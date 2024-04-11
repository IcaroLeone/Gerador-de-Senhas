import random
import string

def generate_password(length=12):
    """Função para gerar uma senha aleatória"""
    # Concatenando letras minúsculas, maiúsculas e dígitos
    characters = string.ascii_letters + string.digits
    # Gerando a senha aleatória
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Bem-vindo ao gerador de senhas!")
    while True:
        try:
            length = int(input("Digite o comprimento da senha desejada (padrão é 12): "))
            break
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    password = generate_password(length)
    print("Sua senha gerada é:", password)

if __name__ == "__main__":
    main()