import secrets
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

print("Bem vindo ao 🔐 Gerador de Senhas Py!")

while True:
    try:
        length = int(input("💡 Dica: O tamanho ideal para uma senha é de no mínimo 8 caracteres!\nTamanho da senha (em números): "))

        if length > 0:
            break
        else:
            print("A senha deve ser maior do que zero. \nTente novamente!")
    
    except ValueError:
        print("Por favor, digite um número válido.")

use_letters = input("Incluir letras? (s/n): ").lower()
use_symbols = input("Incluir símbolos? (s/n): ").lower()
use_numbers = input("Incluir números? (s/n): ").lower()

pool = ""

if use_letters == "s":
    pool += letters

if use_symbols == "s":
    pool += symbols

if use_numbers == "s":
    pool += digits

if pool == "":
    print("Você deve selecionar pelo menos um tipo.")
else:
    password_chars = []

    if use_letters == "s":
        password_chars.append(secrets.choice(letters))

    if use_symbols == "s":
        password_chars.append(secrets.choice(symbols))

    if use_numbers == "s":
        password_chars.append(secrets.choice(digits))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password_chars)

    password = "".join(password_chars)


    print(f"\nSenha gerada: {password}")

