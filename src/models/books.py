from flask_restx import fields

from src.server.instance import server

book = server.api.model('Book', {
    'id': fields.String(description='O Id do Livro'),
    'title': fields.String(required=True, min_length=1, max_length=200, description='O Título do Livro'),
})