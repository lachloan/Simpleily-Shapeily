from sys import argv

shape = input("Shape to create")
capshape = input("Shape with capital letter")

f1 = open('template.py', 'r')
f2 = open(shape + '.py', 'w')
for line in f1:
    f2.write(line.replace('diamond', shape).replace('Diamond', capshape))

f1.close()
f2.close()
