from flask import Flask

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

from App import routes