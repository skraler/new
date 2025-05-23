import random
import string

def generate_password(length=12):
    """Генерирует случайный пароль из букв, цифр и спецсимволов."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = []
    for _ in range(length):
        password.append(random.choice(chars))
    return ''.join(password)
