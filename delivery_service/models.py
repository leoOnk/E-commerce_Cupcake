# 🚚 delivery_service/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Entrega(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer)
    status = db.Column(db.String(50))
    data_envio = db.Column(db.DateTime)
    data_entrega = db.Column(db.DateTime)
