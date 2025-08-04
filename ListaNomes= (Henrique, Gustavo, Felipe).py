ListNames = ['1', '2', '3', '4', '5', '6', '7']

i= int(0)

name= input(str('Type a name: '))

while name !=  str(''):
    
     ListNames.append (name)
     i = (i + 1)
     name= input(str('Type a name: '))

print(ListNames)

ListNames.sort()

print(ListNames)

ListNames.sort(reverse=True)

print(ListNames)

x = 0

while x >= 0 and  x <= len(ListNames):
     
     x= input(str('Check position: '))
     
     try:
          x = int(x)
     except ValueError:
          x = (0)
     else:
          x = int(x)
     
     try:
          ListNames[(x - 1)]
     except IndexError:
          x = -1
     else:
          print(ListNames[(x - 1)])