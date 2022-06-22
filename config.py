import os


SECRET_KEY = 'luan'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'b33c0856db517c',
        senha = 'e34e9305',
        servidor = 'us-cdbr-east-05.cleardb.net',
        database = 'heroku_9e891bd70d69070'
    )
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
