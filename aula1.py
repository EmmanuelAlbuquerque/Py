salario = int(input("salario:"))
imposto = input("imposto:")

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)
sal = salario - (salario * (imposto*0.01))    
print(sal)


#Função em python#

def calculosalario():
    imposto = 27.
    while imposto > 0.:
        imposto = input("imposto ou (s) sair:")
        if not imposto:
            imposto = 27.
        elif imposto == 's':
            break
        else:
            imposto = float(imposto)
            print("Valor final {0}".format(salario - (salario * imposto + 00.1)))

salario = int(input('salario'))

calculosalario()


#FOR PYTHON
for i in range(6):
    print(i)

for i in range(1, 6):
    print(i)