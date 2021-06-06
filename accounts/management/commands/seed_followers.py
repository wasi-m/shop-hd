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
            all_users_df = pd.read_json(f'{BASE_DIR}/data/users.json')
            followers_df = pd.DataFrame(columns=['from_user_id', 'to_user_id'])
            for index, user in all_users_df.iterrows():
                to_user_id = [user[0]]*len(user[1])
                temp_followers_df = pd.DataFrame(columns=['from_user_id', 'to_user_id'])
                temp_followers_df['to_user_id'] = to_user_id
                temp_followers_df['from_user_id'] = user[1]
                followers_df = followers_df.append(temp_followers_df)
            engine = create_engine(f"sqlite:///{str(DATABASES['default']['NAME'])}", echo=False)
            with engine.begin() as connection:
                followers_df.to_sql('accounts_user_following', con=connection, if_exists='append', index=False)
        except Exception as exception:
            raise CommandError('Error' % exception)

        self.stdout.write(self.style.SUCCESS('Successfully added all user followers'))