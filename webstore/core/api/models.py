from django.db import models


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.country} | {self.city}'


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_code = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.phone_code}{self.phone_number}'


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    birthday = models.DateField()
    gender = models.CharField(max_length=45)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

class Type(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.id} | {self.name} | {self.description}'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    state = models.PositiveIntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.username} {self.email} {self.type.name}'

    class Meta:
        verbose_name = 'Usúario'
        verbose_name_plural = 'Usúarios'
        ordering = ['id']


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Name: {self.name}'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Name: {self.name}'


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'Product: {self.product}'


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    session_id = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Session: {self.session_id}'


class ProductCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Cart: {self.cart}'


class Request(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Total price: {self.total_price}'


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.PositiveIntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey(Request, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'State: {self.state}'

