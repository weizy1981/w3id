from flask import Flask
from flask_oidc import OpenIDConnect
import os

filename = 'client_secrets.json'
path = os.path.dirname(__file__)
filepath = os.path.join(path, filename)

app = Flask(__name__)
app.config.update({
    'OIDC_CLIENT_SECRETS': filepath,
    'SECRET_KEY': 'secret'
})

oidc = OpenIDConnect(app)


@app.route('/')
@oidc.require_login
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
