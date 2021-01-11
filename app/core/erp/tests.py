from django.test import TestCase
from app.wsgi import  *
from core.erp.models import Type, Employee

# #Listar
# query = Type.objects.all()
# print(query)

#obj = Type.objects.filter(name__icontains='hel')
# obj = Type.objects.filter(name__startswith='P')
# obj = Type.objects.filter(name__endswith='e')
#obj = Type.objects.filter(name__in=['Hello'])
#obj = Type.objects.all().count()
# obj = Type.objects.filter(name__endswith='o').exclude(id=1)
# for obj in Type.objects.filter(name__startswith='P'):
#     print(obj.name)

Employee.objects.filter(type_id = 1)


# #Insersion
# t = Type(name='Hello')
# #t.name = 'Prueba'
# t.save()

# #Edición
# try:
#     t= Type.objects.get(id=45)
#     t.name = 'Accionista'
#     print((t.name))
# except Exception as e:
#     print(e)

# #Eliminar
# t = Type.objects.get(id =2)
# t.delete()


