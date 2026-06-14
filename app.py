import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from backend.database import db
from backend.routes.auth import auth_bp
from backend.routes.profile import profile_bp
from backend.routes.ai import ai_bp

app = Flask(__name__)

# ---------------- CONFIG ---------------- #
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///placementpro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "placementpro-secret-key"

# ---------------- INIT ---------------- #
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# ---------------- REGISTER ROUTES ---------------- #
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(ai_bp)

# ---------------- HOME ---------------- #
@app.route("/")
def home():
    return {"message": "PlacementPro AI Backend Running"}

# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(debug=True)