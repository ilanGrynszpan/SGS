
import sys
from flask import jsonify, render_template, redirect, url_for, request, abort

from models.paciente import Paciente

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy

def index():
    all = Paciente.query.all()

    for a in all:
        print(Paciente.json(a))

    return {"pacientes":[Paciente.json(paciente) for paciente in Paciente.query.all()]}