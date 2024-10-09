from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='frontend', static_url_path='/')

    # Enable CORS for all routes
    CORS(app)

    # Register routes from routes.py
    from routes import main
    app.register_blueprint(main)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
