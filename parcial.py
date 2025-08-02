from datetime import date

data= date.today()

hj= data.strftime('%d/%m')

#------------------------

meta= input('Qual é a meta de hoje? ')

try:
    meta= float(meta)
except ValueError:
    meta= 0
else:
    meta= float(meta)

metad= input('Qual é a meta desafio de hoje? ')

try:
    metad= float(metad)
except ValueError:
    metad= 0
else:
    metad= float(metad)

mc= input('E a meta de pares? ')

try:
    mc= int(mc)
except ValueError:
    mc= 0
else:
    mc= int(mc)    


#---------------------------

Vendas = input('Quanto Vendemos? ')
try:
    Vendas = float(Vendas)
except ValueError:
    Vendas = float(0)
else:
    Vendas = float(Vendas)
    

#---------------------------


voucher = input('Quanto vendemos voucher? ')

try:
    voucher = float(voucher)
except ValueError:
    voucher = float(0)
else:
    voucher = float(voucher)


#---------------------------


link = input('Temos Venda Link? 1 = sim ')

if link == str(1):
        VendasLink = input('Quanto Vendemos em Link: ')
        try:
                VendasLink = float(VendasLink)
        except ValueError:
                VendasLink = 0.0
        else:
                VendasLink = float(VendasLink)

if link != str(1):
    VendasLink = 0.0


#---------------------------


rct= (Vendas)

#---------------------------

clçds= input('Quantos calçados foram vendidos? ')

try:
    clçds= int(clçds)
except ValueError:
    clçds = 0
else:
    clçds = int(clçds)

bolsas= input('Quantas bolsas foram vendidas? ')

try:
    bolsas= int(bolsas)
except ValueError:
    bolsas = 0
else:
    bolsas = int(bolsas)

acessorios= input('Quantos Acessórios vendemos? ')

try:
    acessorios= int(acessorios)
except ValueError:
    acessorios = 0
else:
    acessorios = int(acessorios)

pa= input('Qual é o PA? ')

try:
    pa= float(pa)
except ValueError:
    pa = 0.0
else:
    pa = float(pa)

tm= input('Qual é o Ticket Médio? ')

try:
    pa= float(pa)
except ValueError:
    pa = 0.0
else:
    pa = float(pa)
    


Total= (Vendas + voucher)

if meta != 0:
    mta= int((Total/meta)*100)


#---------------------------


print('\n\n\n*{}*\n'.format(hj))

print('          *Loja* \n \n')


print('Meta: R${}'.format(meta))
print('Meta de Pares: ',mc, '\n')

print('*META DESAFIO: R$ ',metad, '\n')

print('Receita: R${}'.format(rct))
print('Bolsas: ',bolsas)
print('Pares: ',clçds)
print('Acessórios: ',acessorios)
print('PA: {}'.format(pa))
print('Ticket Médio: R${}'.format(tm))
print('Vouchers: R$:{}'.format(voucher))
print('Vendas Link: R${}'.format(VendasLink))
print('Meta: {}%'.format(mta))
print('\n\n*Total: R${}*\n\n'.format(Total))