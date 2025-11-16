# delivery_service/routes.py

from flask import Blueprint, request, jsonify
from models import db, Entrega

delivery_routes = Blueprint('delivery', __name__)

@delivery_routes.route('/entregas', methods=['GET'])
def listar_entregas():
    entregas = Entrega.query.all()
    return jsonify([{'id': e.id, 'pedido_id': e.pedido_id, 'status': e.status} for e in entregas])

@delivery_routes.route('/entrega', methods=['POST'])
def registrar_entrega():
    data = request.json
    nova_entrega = Entrega(**data)
    db.session.add(nova_entrega)
    db.session.commit()
    return jsonify({'message': 'Entrega registrada'})
