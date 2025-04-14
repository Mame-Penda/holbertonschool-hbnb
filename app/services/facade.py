from werkzeug.security import generate_password_hash, check_password_hash

# Simule une base de données
users_db = {}

class HBnBFacade:
    def __init__(self):
        pass

class User:
    def __init__(self, user_id, first_name, last_name, email, password, is_admin=False):
        self.id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password_hash = generate_password_hash(password)
        self.is_admin = is_admin

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "is_admin": self.is_admin
        }

# 📌 Fonction pour récupérer un utilisateur par email
def get_user_by_email(email):
    return next((user for user in users_db.values() if user.email == email), None)

# 📌 Fonction pour récupérer un utilisateur par ID
def get_user(user_id):
    return users_db.get(user_id)

# 📌 Fonction pour créer un nouvel utilisateur
def create_user(user_data):
    user_id = str(len(users_db) + 1)  # Simule un ID unique
    new_user = User(user_id, **user_data)
    users_db[user_id] = new_user
    return new_user

# 📌 Fonction pour mettre à jour un utilisateur
def update_user(user_id, updated_data):
    user = users_db.get(user_id)
    if user:
        for key, value in updated_data.items():
            setattr(user, key, value)
        return user
    return None
