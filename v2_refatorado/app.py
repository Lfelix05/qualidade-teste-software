import bcrypt
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login_page():
    return render_template('login.html')

class user:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    users = []

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        new_user = user(name, email, password)
        return new_user.add_user()

    @app.route('/add_user', methods=['POST'])
    def add_user(self, password):
        password_bytes = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        self.password = hashed_password

        if len(self.email) < 5 or len(self.password) < 8:
            return jsonify({"message": "Email ou senha inválidos."}), 400
        
        if self.email in [user.email for user in self.users]:
            return jsonify({"message": "Usuário já cadastrado."}), 400
        elif not self.name or not self.email or not self.password:
            return jsonify({"message": "Todos os campos são obrigatórios."}), 400
        else:
            if len(self.name) < 3:
                return jsonify({"message": "Nome deve ter pelo menos 3 caracteres."}), 400
            else:
                self.users.append(self)
                return jsonify({"message": "Usuário cadastrado com sucesso."}), 201

    @app.route('/get_users', methods=['GET'])
    @classmethod
    def get_users(cls):
        return cls.users

    @app.route('/login', methods=['POST'])
    @classmethod
    def login(cls, email, password):
        for user in cls.users:
            if user.email == email and bcrypt.checkpw(password.encode('utf-8'), user.password):
                return True
        return False


if __name__ == "__main__":
    app.run(debug=True)
