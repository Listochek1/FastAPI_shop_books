import random
import string

def generate_secret_key(length=64):
    """
    Генерирует случайный секретный ключ из букв и цифр.
    
    :param length: Длина ключа (по умолчанию 64 символа)
    :return: Строка с секретным ключом
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Пример использования
secret_key = generate_secret_key()
print("Секретный ключ:", secret_key)