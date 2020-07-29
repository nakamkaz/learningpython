def entrance(myname='nakamkaz'):
	print("hello", myname,"san")

def entranceDict(name='Smith',label='AGT.'):
	print(label,"hello",name,"!")


entrance()
entrance(myname='John Do')

apmembers=['Kein','Kine','Keen']

for ap in apmembers:
	entrance(ap)

dict = {"AGT.":"Alex","MGR.":"Philp","R":"C"}

for k,v in dict.items():
	entranceDict(v,k)
