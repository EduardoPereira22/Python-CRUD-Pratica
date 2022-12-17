from flask import Flask

from routes.users import users_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
if __name__ == "__main__":
    app.register_blueprint(users_bp)
    app.run(debug=True)
