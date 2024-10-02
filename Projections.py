from datetime import date

data= date.today()

dia= data.strftime('%d')
dia= int(dia)

mês= data.strftime('%m')

ano= data.strftime('%Y')
ano= int(ano)

hoje= data.strftime('%d/%m')

mês = int(mês)





if mês == (1):
    diamax= (31)


if mês == (2):
    try: 
        int(ano/4)
    except ValueError:
        diamax= (28)
    else:
        diamax= (29)

if mês == (3):
    diamax= (31)

if mês == (4):
    diamax= (30)

if mês == (5):
    diamax= (31)

if mês == (6):
    diamax= (30)

if mês == (7):
    diamax= (31)

if mês == (8):
    diamax= (31)

if mês == (9):
    diamax= (30)

if mês == (10):
    diamax= (31)

if mês == (11):
    diamax= (30)

if mês == (12):
    diamax= (31)
    

print(diamax,hoje,ano)


diasrestantes= (diamax-dia)


Meta =input('Qual é a meta do mês? ')
try:
    Meta= int(Meta)
except ValueError:
    print('Sem entrada para Meta, a meta será definida como 350k')
    Meta= int(350000)
else:
    Meta= int(Meta)
    
    
MetaDia= (Meta/diamax)


Vendas= input('Quanto você vendeu? (lembrando para usar "." em vez de "," ')
try:
    Vendas= float(Vendas)
except ValueError:
    Vendas= float(1)
else:
    Vendas= float(Vendas)


VendasVoucher= input('Quanto você vendeu? (lembrando para usar "." em vez de "," ')
try:
    VendasVoucher= float(VendasVoucher)
except ValueError:
    VendasVoucher= float(0)
else:
    VendasVoucher= float(VendasVoucher)

Vendas= (Vendas+VendasVoucher)

MetaDiaReal= ((Meta-Vendas)/diasrestantes)





