total = totmil = menor = cont = 0
maisbarato = ''
while True:
    produto = str(input('Produto:'))
    preço = float(input('preço: R$'))
    cont += 1
    total += preço
    opçao = ' '
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        maisbarato = produto
    #else:
        #if preço < menor:
            #preço = menor
            #maisbarato = produto
    while opçao not in 'SsNn':
        opçao = str(input('Continuar?:'))
    if opçao in 'Nn':
        break
print('-'*20)
print(f'O total foi de {total}.')
print(f'{totmil} produtos custaram mais que mil reais.')
print(f'{maisbarato} foi o produto mais barato, custando {menor}.')
