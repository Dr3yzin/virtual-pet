def validar_nome(nome):
    try:
        if nome != None and nome[0] != ' ':
            return True

    except:

        return False

def validar_tamanho(nome):
    try:
        if len(nome) <= 10:
            return True

    except:

        return False

