# Jogo da copa
perguntas = [
        {
            'pergunta': 'Em que ano ocorreu a última copa do mundo?',
            'opcoes': [2010, 2013, 2015, 2018],
            'resposta': 2018
        },
        {
            'pergunta': 'Em que ano ocorreu a primeira copa do mundo?',
            'opcoes': [1976, 1940, 1930, 1920],
            'resposta': 1930
        },
        {
            'pergunta': 'Qual foi o primeiro time a ter o título de Campeão mundial?',
            'opcoes': ['Brasil', 'Paraguai', 'Argentina', 'Uruguai'],
            'resposta': 'Uruguai'
        },
]
print()
print('-'*80)
print('Quiz da Copa do Mundo:')
print('-'*80)

acerto = 0
try:
    for i in range(0,3):
        print(f'{i+1})', perguntas[i]['pergunta'])
        print('Opções:')
        for opcao in range(0,4):
            print(f'{opcao + 1}) {perguntas[i]["opcoes"][opcao]}')

        opcao_selecionada = ''

        while True:
            print()
            opcao_selecionada = input("Escolha uma opção: [1, 2, 3, 4] ")
            opcoes = ['1', '2', '3', '4']
            if opcao_selecionada not in opcoes:
                print('Opção digitada inválida!')
                opcao_selecionada = input("Escolha uma opção: [1, 2, 3, 4] ")
            else:
                break   
            
        opcao_respondida = perguntas[i]['opcoes'][int(opcao_selecionada) - 1]
        correta = perguntas[i]['resposta']

        if  opcao_respondida == correta:
            acerto = acerto + 1

    print()

    if acerto == 0:
        print('Que pena você não acertou nenhuma pergunta')
    elif acerto == 1:    
        print(f'Você teve 1 acerto')
    elif acerto > 1:    
        print(f'Você teve {acerto} acertos')

except:
    print(Exception('Valor digitado não é valido, digite uma opção de 1 a 4'))       