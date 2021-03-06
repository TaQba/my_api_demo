from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile("app.cfg")
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)
