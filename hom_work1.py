#0.72
lesen=["matem","fixika","rus yz","bel yz"]
list=lesen
for l in lesen:
    print(l)
col=int(input("сколько предметов не нравится ведите "))
test=0
for i in range(col):
 lesen2=input("веди пердметы которые тебе не нравится: ")
 y=lesen.index(lesen2)
 print(y)
 x=lesen.pop(y)

for l2 in lesen:
    print(l2)