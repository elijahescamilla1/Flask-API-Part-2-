from flask import render_template
from . import inventory_bp

@inventory_bp.route('/cars')
def cars():
    return render_template('cars.html')
