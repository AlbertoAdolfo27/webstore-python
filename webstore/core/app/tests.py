from django.test import TestCase
from webstore.wsgi import *
from core.app.models import Type
from var_dump import var_dump


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
query = Type()
query = Type.objects.filter(name_contains='a')
print(query)
