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
