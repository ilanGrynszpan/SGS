from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    id = db.Column(db.Integer, primary_key=True)
    id_profissional = db.Column(db.Integer)
    nome = db.Column(db.String)
    idade = db.Column(db.Integer)
    endereco = db.Column(db.String)
    diagnostico = db.Column(db.String)

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'endereco': self.endereco,
            'diagnostico': self.diagnostico
        }

        return jsonify(data)

    def __repr__(self):
        return '<Paciente: {}>'.format(self.nome)

    def json(self):
        data = {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'endereco': self.endereco,
            'diagnostico': self.diagnostico
        }
        return(data)
