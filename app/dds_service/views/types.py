from django.shortcuts import render, redirect, get_object_or_404
from ..models import Type
from ..forms.types import TypeForm

def list(request):
    types = Type.objects.all()
    return render(request, 'types/type_list.html', {'types': types})

def create(request):
    if request.method == 'POST':
        form = TypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('types_list')
    else:
        form = TypeForm()
    return render(request, 'types/type_form.html', {'form': form})

def edit(request, pk):
    type_instance = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        form = TypeForm(request.POST, instance=type_instance)
        if form.is_valid():
            form.save()
            return redirect('types_list')
    else:
        form = TypeForm(instance=type_instance)
    return render(request, 'types/type_form.html', {'form': form})

def delete(request, pk):
    type_instance = get_object_or_404(Type, pk=pk)
    if request.method == 'POST':
        type_instance.delete()
        return redirect('types_list')
    return render(request, 'types/type_confirm_delete.html', {'type': type_instance})