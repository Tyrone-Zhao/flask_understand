from models import User


User.verify_auth_token({"id": "1"})
