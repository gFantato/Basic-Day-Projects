ListaNomes= list

i= int(0)

nome= input(str('Digite o nome da pessoa: '))

while nome!=  str(''):
    
     ListaNomes[i] = nome
     i = int(i + 1)
     nome= input(str('Digite o nome da pessoa: '))

print(ListaNomes)