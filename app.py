
from flask import Flask, render_template
from flask_migrate import Migrate

from models.paciente import db
from routes.paciente_bp import paciente_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(paciente_bp, url_prefix='/pacientes')

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
