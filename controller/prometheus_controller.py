from flask import Blueprint

prom_bp = Blueprint('prom_bp', __name__)


@prom_bp.route('/health')
def health():
    return {"status": "UP"}
