from datetime import date

data= date.today()

hj= data.strftime('%d/%m')


#---------------------------


meta= input('Qual é a meta de hoje? ')

try:
    meta= float(meta)
except ValueError:
    meta= 0
else:
    meta= float(meta)


mc= input('E a meta de pares? ')

try:
    mc= int(mc)
except ValueError:
    mc= 0
else:
    mc= int(mc)    


#---------------------------


V1= input('Quanto Vendedor 1 vendeu? ')

try:
    V1= float(V1)
except ValueError:
    V1 = 0.0
else:
    V1 = float(V1)
    

V2= input('Quanto Vendedor 2 vendeu? ')

try:
    V2= float(V2)
except ValueError:
    V2 = 0.0
else:
    V2 = float(V2)
    
    
V3= input('Quanto Vendedor 3 vendeu? ')

try:
    V3= float(V3)
except ValueError:
    V3= 0.0
else:
    V3= float(V3)
    
V4= input('Quanto Vendedor 4 vendeu? ')

try:
    V4= float(V4)
except ValueError:
    V4= 0.0
else:
    V4= float(V4)
    
V5= input('Quanto Vendedor 5 vendeu? ')

try:
    V5= float(V5)
except ValueError:
    V5 = 0.0
else:
    V5 = float(V5)
    

#---------------------------


voucher= input('Temos Venda voucher? 1 = sim ')

if voucher== str(1):
        V1V= input('Vouchers Vendedor 1: ')
        try:
                V1V= float(V1V)
        except ValueError:
                V1V= 0.0
        else:
                V1V= float(V1V)



        V2V= input('Vouchers Vendedor 2: ')
        try:
                V2V= float(V2V)
        except ValueError:
                V2V= 0.0
        else:
                V2V= float(V2V)



        V3V= input('Vouchers Vendedor 3: ')
        try:
                V3V= float(V3V)
        except ValueError:
                V3V= 0.0
        else:
                V3V= float(V3V)



        V4V= input('Vouchers Vendedor 4: ')
        try:
                V4V= float(V4V)
        except ValueError:
                V4V= 0.0
        else:
                V4V= float(V4V)



        V5V= input('Vouchers Vendedor 5: ')
        try:
                V5V= float(V5V)
        except ValueError:
                V5V= 0.0
        else:
                V5V= float(V5V)


#---------------------------


link= input('Temos Venda Link? 1 = sim ')

if link== str(1):
        VendasLink = input('Quanto Vendemos em Link: ')
        try:
                VendasLink= float(VendasLink)
        except ValueError:
                VendasLink= 0.0
        else:
                VendasLink= float(VendasLink)

if link != str(1):
    VendasLink= 0.0


#---------------------------


rct= (V1+V2+V3+V4+V5)

mta= 0


vchrs= 0.0

if voucher== str(1):
    vchrs= (V1V+V2V+V3V+V4V+V5V)


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
    

if vchrs != 0.0:
    
    V1= V1+V1V
    V2= V2+V2V
    V3= V3+V3V
    V4= V4+V4V
    V5= V5+V5V

Total= (V1+V2+V3+V4+V5)

if meta != 0:
    mta= int((Total/meta)*100)


#---------------------------


print('\n\n\n*{}*\n'.format(hj))

print('          *Loja* \n \n')


print('Meta: R${}'.format(meta))
print('Meta de Pares: ',mc, '\n')

print('Receita: R${}'.format(rct))
print('Bolsas: ',bolsas)
print('Pares: ',clçds)
print('Acessórios: ',acessorios)
print('PA: {}'.format(pa))
print('Ticket Médio: R${}'.format(tm))
print('Vouchers: R$:{}'.format(vchrs))
print('Vendas Link: R${}'.format(VendasLink))
print('Meta: {}%'.format(mta))
print('\n\n*Total: R${}*\n\n'.format(Total))


#---------------------------


if V1 != 0.0:
    print('Vendedor 1: R${}'.format(V1))


if V2 != 0.0:
    print('Vendedor 2: R${}'.format(V2))
    

if V3 != 0.0:
    print('Vendedor 3: R${}'.format(V3))


if V4!= 0.0:
    print('Vendedor 4: R${}'.format(V4))


if V5 != 0.0:
    print('Vendedor 5: R${}'.format(V5))
