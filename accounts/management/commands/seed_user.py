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
            all_users_df = pd.read_json(f'{BASE_DIR}/data/names.json')
            all_users_df = all_users_df.rename(columns = {'name':'username'})
            all_users_df['is_superuser'], all_users_df['is_staff'], all_users_df['is_active']  = False, False, True
            all_users_df['first_name'], all_users_df['last_name'], all_users_df['email'] = '','',''
            all_users_df['last_login'], all_users_df['date_joined'] = datetime.now(), datetime.now()
            all_users_df['password'] = make_password('password')
            del all_users_df['id']
            engine = create_engine(f"sqlite:///{str(DATABASES['default']['NAME'])}", echo=False)
            with engine.begin() as connection:
                all_users_df.to_sql('accounts_user', con=connection, if_exists='append', index=False)
        except Exception as exception:
            raise CommandError('Error' % exception)

        self.stdout.write(self.style.SUCCESS('Successfully added all users'))