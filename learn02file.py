f = open('datafile','r')
print(f.readline())
f.close()

f2 = open('outfile','a')
byten = f2.tell()
f2.write("write test append mode\n")
f2.close()

f3 = open('outfile','r')
print("! call readline at 1")
print(f3.readline())
f3.tell()
print("! call readline at 2")
print(f3.readline())
f3.tell()
f3.close()
f4 = open('outfile','r')
print("! call readlines()")
print(f4.readlines())
f4.close()
f5 = open('outfile','r')
print("! call readlines() in for statement")
nl=1
for l1 in f5.readlines():
    print(nl,": ",l1)
    nl=nl+1

f5.close()
