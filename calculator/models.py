from django.db import models


class DiscountRules(models.Model):
    CONSUMER_TYPE_CHOICES = [
        ('Residencial', 'Residencial'),
        ('Comercial', 'Comercial'),
        ('Industrial', 'Industrial'),
    ]

    CONSUMPTION_RANGE_CHOICES = [
        ('<10000', '<10000'),
        ('10000-20000', '10000-20000'),
        ('>20000', '>20000'),
    ]

    consumer_type = models.CharField(max_length=50, choices=CONSUMER_TYPE_CHOICES)
    consumption_range = models.CharField(max_length=50, choices=CONSUMPTION_RANGE_CHOICES)


class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    #  create the foreign key for discount rule model here
    tax_type = models.ForeignKey(DiscountRules, on_delete=models.CASCADE)


# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type        x
-> Consumption range    x
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
