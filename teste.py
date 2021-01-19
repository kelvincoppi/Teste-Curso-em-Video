def not_string(nome):
    if len(nome) >= 3 and nome[:3] == 'not':
        return print(nome)
    return print('not ' + nome)

nome = 'not safe'
not_string(nome)
