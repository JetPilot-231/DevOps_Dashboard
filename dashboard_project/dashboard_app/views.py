# dashboard_app/views.py
from django.shortcuts import render
from .models import User, Metric

def dashboard_home(request):
    users = User.objects.all()
    metrics = Metric.objects.all()
    context = {'users': users, 'metrics': metrics}
    return render(request, 'dashboard_app/dashboard_home.html', context)
