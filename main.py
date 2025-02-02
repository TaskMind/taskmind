from flask import Flask
from routes.pages import bp as bpPages

app = Flask(__name__)

app.register_blueprint(bpPages)
