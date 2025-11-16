# payment_service/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer)
    metodo = db.Column(db.String(50))
    status = db.Column(db.String(50))
    valor = db.Column(db.Numeric(10,2))
