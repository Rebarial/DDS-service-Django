from django.shortcuts import render, redirect, get_object_or_404
from ..models import Transaction, Status, Type, Category, Subcategory
from dds_service.forms.transactions import TransactionForm
from django.utils import timezone

def list(request):
    transactions = Transaction.objects.select_related('subcategory', 'category', 'type', 'status').all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def create(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            print("in transaction")
            if not transaction.date_created:
                print("im realy created")
                transaction.date_created = timezone.now()
            transaction.save()
            return redirect('/')
    else:
        form = TransactionForm(initial={'date_created': timezone.now()})
        form.date_created = timezone.now().strftime('%Y-%m-%dT%H:%M')
        print(form.date_created)

    action = "create"
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()


    return render(request, 'transactions/transaction_form.html', {
        'action': action,
        'form': form,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    })


def edit(request, pk):
    transaction = get_object_or_404(Transaction, id=pk)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction) 
        
        if form.is_valid(): 
            form.save() 
            return redirect('transactions/transaction_list')  
    else:
        form = TransactionForm(instance=transaction) 
        form.date_created = timezone.now().strftime('%Y-%m-%dT%H:%M')

    action = "edit"
    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request, 'transactions/transaction_form.html', {
        'action': action,
        'form': form,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
    })

def delete(request, pk):
    transaction = Transaction.objects.get(pk=pk)
    
    if request.method == "POST":
        transaction.delete()
        return redirect('transaction_list')

    return render(request, 'transactions/transaction_confirm_delete.html', {'transaction': transaction})