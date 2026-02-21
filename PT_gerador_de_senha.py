import secrets
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print("Bem vindo ao 🔐 Gerador de Senhas Py!")

while True:
    try:
        length = int(input("Tamanho da senha: "))

        if length > 0:
            break
        else:
            print("A senha deve ser maior do que zero \nTente novamente!")
    
    except ValueError:
        print("Por favor, digite um número válido.")

use_letters = input("Incluir letras? (s/n): ").lower()
use_symbols = input("Incluir símbolos? (s/n): ").lower()
use_numbers = input("Incluir números? (s/n): ").lower()

pool = ""

if use_letters == "y":
    pool += letters

if use_symbols == "y":
    pool += symbols

if use_numbers == "y":
    pool += digits

if pool == "":
    print("Você deve selecionar pelo menos um tipo.")
else:
    password_chars = []

    if use_letters == "y":
        password_chars.append(secrets.choice(letters))

    if use_symbols == "y":
        password_chars.append(secrets.choice(symbols))

    if use_numbers == "y":
        password_chars.append(secrets.choice(digits))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)


    print(f"\nSenha gerada: {password}")

