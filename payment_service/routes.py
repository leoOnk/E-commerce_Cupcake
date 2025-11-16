# payment_service/routes.py

from flask import Blueprint, request, jsonify
from models import db, Pagamento

payment_routes = Blueprint('payment', __name__)

@payment_routes.route('/pagamentos', methods=['GET'])
def listar_pagamentos():
    pagamentos = Pagamento.query.all()
    return jsonify([{'id': p.id, 'pedido_id': p.pedido_id, 'metodo': p.metodo, 'status': p.status, 'valor': float(p.valor)} for p in pagamentos])

@payment_routes.route('/pagamento', methods=['POST'])
def registrar_pagamento():
    data = request.json
    novo_pagamento = Pagamento(**data)
    db.session.add(novo_pagamento)
    db.session.commit()
    return jsonify({'message': 'Pagamento registrado'})
