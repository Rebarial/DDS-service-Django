from django.shortcuts import render, redirect, get_object_or_404
from dds_service.models import Status
from dds_service.forms.statuses import StatusForm

def list(request):
    statuses = Status.objects.all()
    return render(request, 'statuses/status_list.html', {'statuses': statuses})

def create(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('statuses_list')
    else:
        form = StatusForm()
    return render(request, 'statuses/status_form.html', {'form': form})

def edit(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('statuses_list')
    else:
        form = StatusForm(instance=status)
    return render(request, 'statuses/status_form.html', {'form': form})

def delete(request, pk):
    status = get_object_or_404(Status, pk=pk)
    if request.method == 'POST':
        status.delete()
        return redirect('statuses_list')
    return render(request, 'statuses/status_confirm_delete.html', {'status': status})