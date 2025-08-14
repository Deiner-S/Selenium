from cryptography.fernet import Fernet

# Gerar chave secreta
key = Fernet.generate_key()
print(f"Guarde essa chave: {key.decode()}")  # Você vai precisar dela para descriptografar

fernet = Fernet(key)

# Ler arquivo original
with open('login.txt', 'rb') as file:
    data = file.read()

# Criptografar
encrypt_data = fernet.encrypt(data)

# Salvar arquivo criptografado
with open('encrypt_login.txt', 'wb') as file:
    file.write(encrypt_data)