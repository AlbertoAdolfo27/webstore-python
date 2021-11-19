from django.db import models


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'address'
        verbose_name_plural = 'addresses'

    def __str__(self):
        return f'{self.country} | {self.city}'


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone_code = models.CharField(max_length=45)
    phone_number = models.CharField(max_length=45)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'

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
    address = models.OneToOneField(Address, on_delete=models.PROTECT, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'person'
        verbose_name_plural = 'persons'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class UserType(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'user type'
        verbose_name_plural = 'user types'

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
    person = models.ForeignKey(Person, on_delete=models.PROTECT, null=True)
    usertype = models.OneToOneField(UserType, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.username} {self.email} {self.user_type.name}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['id']


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return f'Name: {self.name}'


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    products = models.ManyToManyField(Product, verbose_name='products')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return f'Name: {self.name}'


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    session_id = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    products = models.ManyToManyField(Product, verbose_name='products')

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'

    def __str__(self):
        return f'Session: {self.session_id}'


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.PositiveIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'Total price: {self.total_price}'


class Payment(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.PositiveIntegerField(default=1)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    order = models.OneToOneField(Order, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'payment'
        verbose_name_plural = 'payments'

    def __str__(self):
        return f'State: {self.state}'

