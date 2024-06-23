from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('car_inventory.config.Config')

    with app.app_context():
        from .auth import auth_bp
        from .inventory import inventory_bp

        app.register_blueprint(auth_bp)
        app.register_blueprint(inventory_bp)

        return app
