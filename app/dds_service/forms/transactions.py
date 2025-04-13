from django import forms
from ..models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date_created', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
        
    def clean(self):
        cleaned_data = super().clean()
        
        type_value = cleaned_data.get('type')
        category_value = cleaned_data.get('category')
        subcategory_value = cleaned_data.get('subcategory')

        if category_value and type_value:
            if category_value.type != type_value:
                self.add_error("category", "Выбранная категория не соответствует выбранному типу.")

        if subcategory_value and category_value:
            if subcategory_value.category != category_value:
                self.add_error("subcategory", "Выбранная подкатегория не соответствует выбранной категории.")

        return cleaned_data
    