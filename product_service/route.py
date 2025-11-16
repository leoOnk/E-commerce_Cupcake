# product_service/routes.py

from flask import Blueprint, request, jsonify
from models import db, Produto

product_routes = Blueprint('product', __name__)

@product_routes.route('/produtos', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{'id': p.id, 'nome': p.nome, 'descricao': p.descricao, 'estoque': p.estoque} for p in produtos])

@product_routes.route('/produto', methods=['POST'])
def adicionar_produto():
    data = request.json
    novo_produto = Produto(**data)
    db.session.add(novo_produto)
    db.session.commit()
    return jsonify({'message': 'Produto adicionado com sucesso'})
