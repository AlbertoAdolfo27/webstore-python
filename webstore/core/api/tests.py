from urllib import request

from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from requests import request

from core.app.utils.Server import Server
from webstore import settings
from webstore.wsgi import *

from var_dump import var_dump

from core.api.models import UserType, Category
from core.api.models import User
from core.api.models import Address
from core.api.models import Contact
from core.api.models import Person


# Query all Type
# queryType = Type.objects.all()
# print(queryType)

# Query Where
# queryType = Type.objects.get(id=1)
# queryType = Type.objects.get(pk=1)
# print(queryType)

# Insertion Type
# t1 = Type()
# t1.id = 1
# t1.name = 'Administrator'
# t1.save()
#
# t2 = Type()
# t2.id = 2
# t2.name = 'Client'
# t2.save()

# delete
# query = Type.objects.get(pk=1)
# query.delete()

# Filter
# query = Type()
# query = Type.objects.filter(id=1)
# print(query)

#
# address = Address(
#     country='Mozambique',
#     city='Beira'
# )
# address.save()
# address = Address.objects.latest('id')
#
# contact = Contact(
#     phone_code='258',
#     phone_number='855004233'
# )
# contact.save()
# contact = Contact.objects.latest('id')
#
#
# person = Person(
#     firstname='Alberto',
#     lastname='Adolfo',
#     birthday='1997-04-27',
#     gender='M',
#     contact=contact,
#     address=address
# )
# person.save(force_insert=True)
# person = Person.objects.latest('id')
#
# type = Type()
# type = Type.objects.get(id=2)
#
# user = User(
#     person=person,
#     username='alberto',
#     email='alberto@example.com',
#     password='123',
#     type=type
# )
# user.save(force_insert=True)


# print(person)
#
# user = User.objects.select_related('person', 'type');
# print(user)


# import requests
#
#
# def buscar_dados():
#     request = requests.get("http://127.0.0.1:8080/api/categories/")
#     print((request).json())
#
#
# print(buscar_dados())

#gquery many to many

# c = Category.objects.all()
# for p in c:
#     print(p.products.all())

# print(reverse('api:category-list'))

# print(Server.get_url('app:admin-product-list'))


# def myFun(*kwargs):
#     for value in kwargs:
#         print(f'{value}')
#
#
# # Driver code
# myFun('Geeks', 'for', 'Geeks')

from django.http import request

