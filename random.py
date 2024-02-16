import random
#........random..............
'''
num = random.randint(0, 2)
complayer = "sang"



print(num)
'''
#............end...........

dr = "my name is {:6d} and im all".format(555)
print(dr)


x = input("convert decimal to binary")
v = x + " in binary is {:b}".format(int(x))
print(v)


n = input("convert decimal to octal")
f = n + " in octal is {:o}".format(int(n))
print(f)


c = input("convert decimal to hexadecimal")
b = c + " in hexadecimal is {:x}".format(int(c))
print(b)

