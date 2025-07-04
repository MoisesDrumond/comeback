#type: ignore
from flask import Blueprint, render_template, request
from database.cliente import Clientes

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html', clientes=Clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    
    data = request.json

    novo_usuario = {
        "id": len(Clientes) + 1,
        "nome": data['nome'],   
        "email": data['email'],
    }

    Clientes.append(novo_usuario)

    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def edit_form_cliente(cliente_id):
    return render_template('edit_form_cliente.html')

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    global Clientes
    Clientes = [ c for c in Clientes if c['id'] != cliente_id ]

    return{'deleted': 'ok'}
