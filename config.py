import os


SECRET_KEY = 'luan'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'b2259be377ae62',
        senha = '3803dd2f',
        servidor = 'us-cdbr-east-05.cleardb.net',
        database = 'heroku_b8bfc4054fcd6c0'
    )
#mysql://:@/?reconnect=true
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
