#o.73
num=4
c=0
pludo=[]
for i in range(num):
 pludo1=input("ведите 4 блюда ")
 pludo.append(pludo1)
for i in pludo:
 print(pludo.index(i),i)
otvet=input("хотите удолить блядо? yes/no ")
if otvet=='yes':
 num2=int(input("какое блюдо хртите удолить? "))
 pludo.pop(num2)
 pludo.sort()
 for i in pludo:
     print(i)
 else:
     print("спасибо за выбор")


