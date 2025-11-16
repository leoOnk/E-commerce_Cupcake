# order_service/routes.py

from flask import Blueprint, request, jsonify
from models import db, Pedido

order_routes = Blueprint('order', __name__)

@order_routes.route('/pedidos', methods=['GET'])
def listar_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{'id': p.id, 'cliente_id': p.cliente_id, 'status': p.status, 'data': p.data, 'valor': float(p.valor)} for p in pedidos])

@order_routes.route('/pedido', methods=['POST'])
def criar_pedido():
    data = request.json
    novo_pedido = Pedido(**data)
    db.session.add(novo_pedido)
    db.session.commit()
    return jsonify({'message': 'Pedido criado com sucesso'})
