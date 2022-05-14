'''dic = {'tipo' : 'assim' , 'preco' : [10,[1,2]]}
print(dic)
print(dic['tipo'])
print(dic['preco'])
dic['quantidade'] = 13
print(dic)'''


class caneca:
    tipo = ''
    cor = ''
    nome = ''

    def beber(self):
        print('Beber da caneca ' , self.nome)


caneca1 = caneca()
caneca1.tipo = 'Tipo'
caneca1.cor = 'Cor'
caneca1.nome = 'Nome'

print(caneca1.tipo, caneca1.cor, caneca1.nome)
caneca1.beber()

caneca.tipo = 'padrão'
caneca2 = caneca()
print(caneca2.tipo)