from django.db import models

class Base(models.Model):

    class Meta:
        abstract = True

    def __str__(self):
        result = f"{self.__class__.__name__}: "
        for field in self._meta.get_fields():
            result += f"{field.name} = {getattr(self, field.name)}; "
        return result

class BaseTypeModel(Base):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Status(BaseTypeModel):
    pass

class Type(BaseTypeModel):
    pass

class Category(BaseTypeModel):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

class Subcategory(BaseTypeModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Transaction(Base):

    date_created = models.DateTimeField() 
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)