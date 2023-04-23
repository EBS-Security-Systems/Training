# Declarando e inicializando as variáveis para cada propriedade da conta:
proprietario = 'Thiago Sousa'
agencia = 888
digito_agencia = 8
conta = 88888
digito_conta = 8
saldo = 5000.00
senha = 1478

# Inicializando o sistema


# Fazendo um título com estilo :)
print('-' * 50) # Curiosidade: vc está pedindo ao python aqui que ele escreva um traço 50 vezes
print('     Banco da Brasília - Página de Login    ')
print('-' * 50)

# Dando instruções ao usuário sobre o que fazer
print('Olá! Para acessar sua conta virtualmente é necessário inserir alguns dados: ')
ag = int(input('Agência: '))
dag = int(input('Dígito da agência: '))

# Aqui estamos simulando uma consulta numa ampla variedade de registros.
# Lembrando que aqui tem-se somente um registro de agência existente, pois é um sistema de um banco imaginário

if(ag != agencia or dag != digito_agencia): # Se os valores informados são diferentes dos existentes...
    print('\nAgência não encontrada!\nEncerrando o sistema...') # Curiosidade: O caractere \n pula uma linha em uma String
    # Tente usar \t pra ver o que acontece
else:
    print('\nAgência detectada:\nMogi das Cruzes - SP')
    c = int(input('\nDigite o nº da conta: '))
    dc= int(input('Agora, informe o dígito: '))

    if(c != conta or dc != digito_conta): # Se os valores informados são diferentes das possibilidades já conhecidas...
        print('\nEsta conta não foi encontrada nesta agência!\nEncerrando o sistema...')
    else:
        print('\nConta encontrada')
        s = int(input('Informe a sua senha: '))
        if (s == senha): # Caso a senha estea correta...
            print('\n' + '-' * 50)
            print(f"Olá {proprietario}! Seja bem vindo!")
            print(f"Agência: {agencia}-{digito_agencia}\nConta: {conta}-{digito_conta}")
            print('\nSeu saldo é R$' + str(saldo))
        else:
            print('\nSenha incorreta!\nEncerrando o sistema por tentativa de invasão!')
            # Curiosidade: Encerar o sistema ou recarregar a página no caso de errar a senha deixa o sistema mais resiliente contra ataques de força bruta
            # Pesquise sobre Wordlists em Python e aprenda a hackear de verdade!!!
