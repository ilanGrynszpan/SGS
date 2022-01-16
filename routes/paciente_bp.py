from flask import Blueprint

from controllers.paciente_controller import index

paciente_bp = Blueprint('paciente_bp', __name__)

paciente_bp.route('/', methods=['GET'])(index)