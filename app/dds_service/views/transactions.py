from django.shortcuts import render, redirect, get_object_or_404
from ..models import Transaction, Status, Type, Category, Subcategory
from dds_service.forms.transactions import TransactionForm
from django.utils import timezone
from django.db.models import Q

def list(request):
    transaction_status = request.GET.get('status')
    transaction_type = request.GET.get('type')
    transaction_category = request.GET.get('category')
    transaction_subcategory = request.GET.get('subcategory')

    query = Q()

    if transaction_status:
        query &= Q(status=transaction_status)

    if transaction_type:
        query &= Q(type=transaction_type)

    if transaction_category:
        query &= Q(category=transaction_category)
    
    if transaction_subcategory:
        query &= Q(subcategory=transaction_subcategory)

    statuses = Status.objects.all()
    types = Type.objects.all()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    transactions = Transaction.objects.select_related('subcategory', 'category', 'type', 'status').filter(query)

    return render(request, 'transactions/transaction_list.html', {
        'transactions': transactions,
        'statuses': statuses,
        'types': types,
        'categories': categories,
        'subcategories': subcategories,
        })

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