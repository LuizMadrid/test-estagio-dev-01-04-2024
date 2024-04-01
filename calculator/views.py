from django.shortcuts import render

from calculator.models import DiscountRules
from .models import Consumer

# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database --nao consegui
-> Get the discount value for each consumer
-> Calculate the economy --tentei
-> Send the data to the template that will be rendered
"""


def calculate_savings(consumer):
    average = consumer.consumption
    rule = DiscountRules.objects.get(consumer_type=consumer.tax_type, consumption_range=average)
    discount = rule.discount_value * rule.cover_value * average * consumer.distributor_tax
    return discount


def view1(request):
    # Create the first view here.
    consumers = Consumer.objects.all()
    for consumer in consumers:
        consumer.savings = calculate_savings(consumer)
        consumer.save()
    return render(request, 'calculator/list.html', {'consumers': consumers})


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass
