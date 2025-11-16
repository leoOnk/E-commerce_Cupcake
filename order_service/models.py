from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer)
    status = db.Column(db.String(50))
    data = db.Column(db.DateTime)
    valor = db.Column(db.Numeric(10,2))
