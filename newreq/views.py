from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import RequestForm
from .models import Call
from .tasks import update_model
from datetime import datetime, timedelta
from django.urls import reverse


@login_required
def requests(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            req_date = form.cleaned_data['req_date']
            req = Call(
                user = request.user.id,
                url = url,
                req_date = req_date,
            )
            req.save()

            execution_datetime = datetime.strptime(req_date, '%d-%m-%Y %H:%M')
            execution_datetime = execution_datetime - timedelta(hours=1) # hack for Celery TZ not changing
            update_model.apply_async((url, req.id), eta=execution_datetime)
            return HttpResponseRedirect(reverse('history'))
        else:
            return render(request, 'requests/requests.html', context={'form': form})
    else:
        return render(request, 'requests/requests.html', context={'form': RequestForm()})