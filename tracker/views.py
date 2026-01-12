from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import StudyLog

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')


@login_required
def dashboard(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        topic = request.POST.get('topic')

        if action == 'start':
            StudyLog.objects.create(
                user=request.user,
                topic=topic,
                start_time=timezone.now()
            )

        elif action == 'end':
            log = StudyLog.objects.filter(
                user=request.user,
                end_time__isnull=True
            ).last()

            if log:
                log.end_time = timezone.now()
                log.save()

        return redirect('dashboard')

    logs = StudyLog.objects.filter(user=request.user).order_by('-start_time')
    active_log = logs.filter(end_time__isnull=True).first()

    return render(request, 'dashboard.html', {
        'logs': logs,
        'active_log': active_log
    })
