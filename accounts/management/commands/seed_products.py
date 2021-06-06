import json
from django.core.management.base import BaseCommand, CommandError
from accounts.models import User
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime

from shop.settings import BASE_DIR, DATABASES
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            all_products_df = pd.read_json(f'{BASE_DIR}/data/products.json')
            columns = {
                'productName':'name','productCategory':'category','productImage':'image',
                'productStock':'stock','productPrice':'price','salePrice':'saleprice'}
            all_products_df = all_products_df.rename(columns = columns)
            del all_products_df['productId']
            print(all_products_df)
            engine = create_engine(f"sqlite:///{str(DATABASES['default']['NAME'])}", echo=False)
            with engine.begin() as connection:
                all_products_df.to_sql('products_product', con=connection, if_exists='append', index=False)
        except Exception as exception:
            raise CommandError('Error' % exception)

        self.stdout.write(self.style.SUCCESS('Successfully added all products'))
