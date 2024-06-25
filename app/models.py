from django.db import models
from parler.models import TranslatableModel,TranslatedFields
from django.contrib.auth.models import AbstractUser

class Table(models.Model):
    number =models.IntegerField()

    def str(self):
        return f"{self.number}"

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    peple_count =models.IntegerField()
    price_v1 =models.FloatField()
    price_v2 =models.FloatField()
    total_price =models.FloatField()

class Category(TranslatableModel):
    translations = TranslatedFields(
        cat_name = models.CharField(("Name"), max_length=100)

    )

    def __str__(self):
        return f"{self.safe_translation_getter('cat_name')}"

class MenuItem(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100),
        description = models.TextField()
    )
    image = models.ImageField(upload_to='Food/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)    
    price = models.FloatField()

    def str(self):
        return f"{self.safe_translation_getter('name')}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    count = models.PositiveIntegerField()

    def str(self):
        return f"{self.order.name}"