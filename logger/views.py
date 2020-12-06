from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from newreq.models import Call


@login_required
def history(request):
    processed_requests = Call.objects.filter(user=request.user.id, processed=True)
    unprocessed_requests = Call.objects.filter(user=request.user.id, processed=False)
    context = {
        'processed': processed_requests,
        'unprocessed': unprocessed_requests,
    }
    return render(request, 'logger/history.html', context=context)