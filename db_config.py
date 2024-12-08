import datetime
import logging
import os
import sys
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from playhouse.db_url import connect


load_dotenv(override=True)

# ログを出力する設定
logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db = connect(os.environ.get("DATABASE"))

# メッセージモデル
class Message(Model):
    """MessageModel"""
    id = IntegerField(primary_key=True)
    user = CharField()
    content = TextField()
    pub_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = db
        table_name ="messages"

db.create_tables([Message])
    

    

