print('Este programa decidirá se você foi multado ou não')
velocidade = int(input('Digite a velocidade do seu carro: '))
multa = velocidade * 7
if velocidade >80:
    print('Você foi multado em R${:.2f}'.format(multa))
    print('irmão.... tu ta multado, tu andou a 80 por hora na rua da dona fatima senhora de 90 anos que se qualquer barulho alto pode morrer do coração')
elif velocidade == 80:
    print('Escapo em..... to vendo issai, to de olho na proxima eu dou mais um empurraozinho nesse seu carro quero ver')
else:
    print('Bom, você é uma boa tartaruga, senta o pé pela mor de deus')