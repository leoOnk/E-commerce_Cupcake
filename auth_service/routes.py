# auth_service/routes.py

from flask import Blueprint, request, jsonify
from models import db, Cliente

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json
    novo_cliente = Cliente(nome=data['nome'], email=data['email'], senha=data['senha'])
    db.session.add(novo_cliente)
    db.session.commit()
    return jsonify({'message': 'Cliente registrado com sucesso'})

@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json
    cliente = Cliente.query.filter_by(email=data['email'], senha=data['senha']).first()
    if cliente:
        return jsonify({'message': 'Login bem-sucedido'})
    return jsonify({'message': 'Credenciais inválidas'}), 401
