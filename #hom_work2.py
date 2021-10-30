#0.76
nam=3
namelist=[]
for i in range(nam):
  print(i)
  name=input("ведите 2 имена кого хотите пригласить ")
  namelist.append(name)

for i in namelist:
  print(i)
while True:
 print("вы хотите добавить имя?yes/no")
 ot=input()
 if ot=='yes':
   name=input("ведите имя ")
   namelist.append(name)
 elif ot=='no':
   for i in namelist:
     print(i)



