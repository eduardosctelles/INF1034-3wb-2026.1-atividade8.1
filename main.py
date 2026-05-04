from pygame import *
import sys

clock = time.Clock()

def val_email(email):
    return email[-8:] == '@puc.com'

def maiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z':
            return True
    return False

def minuscula(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'a':
            return True
    return False

def num(palavra):
    for carac in palavra:
        if '0' <= carac <= '9':
            return True
    return False

def val_senha(senha):
    return len(senha) >= 8 and maiuscula(senha) == True and minuscula(senha) == True and num(senha) == True

def criptografia(senha):
    senha_cripto = ""
    for char in senha:
        if char.isdigit():
            pass
        elif 'A' <= char <= 'Z':
            ref = ord('A') # 65
            ascii_char = ord(char) # Etapa 1
            pos_alpha = ascii_char - ref # Etapa 2
            pos_cesar = pos_alpha + 3 # Etapa 3
            pos_cesar = pos_cesar % 26 # Etapa 4
            letra_cesar = chr(ref + pos_cesar) # Etapa 5
            senha_cripto += letra_cesar
        elif 'a' <= char <= 'z':
            pass
        else:
            senha_cripto += char
    return senha_cripto

email = input('Digite o seu email:\n')
senha = input('Digite a sua senha:\n')

if val_email('dudetelles@puc.com') == True and val_senha('Johnwilliams1977') == True:
    janela = display.set_mode((800, 800))
    janela.fill((255, 255, 255))
    init()
    running = True
    while running: 
        fonte = font.Font('fonte.ttf', 50)
        clock.tick(60)
        for ev in event.get():
            if ev.type == QUIT:
                running = False
else:
    print('Acesso negado!')