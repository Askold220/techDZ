import os


class Config:
    SECRET_KEY = os.environ.get('13579')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:135300**@localhost/internet_shop'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #mysql://username:password@server/db

# print(Config.SECRET_KEY)