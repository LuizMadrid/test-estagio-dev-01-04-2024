from django.core.management.base import BaseCommand
import pandas as pd
from calculator.models import Consumer, DiscountRules


class Command(BaseCommand):
    help = 'Load consumers from Excel file'

    def handle(self, *args, **options):
        df = pd.read_excel('consumers.xlsx')
        for index, row in df.iterrows():
            rule = DiscountRules.objects.get(consumer_type=row['consumer_type'],
                                             consumption_range=row['consumption_range'])

            consumer = Consumer(name=row['name'],
                                consumption=row['consumption'],
                                distributor_tax=row['distributor_tax'],
                                tax_type=rule)

            consumer.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded consumers'))
