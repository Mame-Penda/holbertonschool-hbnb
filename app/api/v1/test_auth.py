import requests

# URL de ton serveur Flask
BASE_URL = "http://127.0.0.1:5000"

# Créer un utilisateur et obtenir un token
def get_token():
    login_url = "http://127.0.0.1:5000/auth/login"  # Adapte l'URL à ton endpoint d'authentification
    credentials = {
        "email": "admin@example.com",
        "password": "adminpassword"
    }
    
    response = requests.post(login_url, json=credentials)
    if response.status_code == 200:
        return response.json().get("access_token")  # Vérifie que ton API retourne bien "access_token"
    else:
        print(f"Erreur d'authentification: {response.json()}")
        return None

# Vérifier une route protégée
def test_protected_route():
    token = get_token()
    if not token:
        print("Impossible d'obtenir un token JWT.")
        return
    
    headers = {"Authorization": f"Bearer {token}"}
    protected_url = f"{BASE_URL}/admin/users/"  # Adapte cette route selon ton API

    response = requests.get(protected_url, headers=headers)
    
    if response.status_code == 200:
        print("✅ Accès autorisé:", response.json())
    elif response.status_code == 403:
        print("🚫 Accès refusé (droits insuffisants)")
    else:
        print(f"❌ Erreur: {response.status_code} - {response.json()}")

if __name__ == "__main__":
    test_protected_route()
