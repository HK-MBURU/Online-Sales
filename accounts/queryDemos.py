from crm1.accounts.models import *


customers=Customer.objects.all()
firstCustomer=customers.objects.first()
lastCustomer=customers.objects.last()
