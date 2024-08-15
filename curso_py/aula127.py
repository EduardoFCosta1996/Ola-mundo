s1 = set()
s1.add("eduardo")
s1.update(('Costa',))
s1.discard("eduardo")
print(s1)
#for numero in s1:
    #print(numero)

s2 = {1,2,3}
s3 = {4,2,5,6}
s4 = s2|s3
s5= s2&s3
s6 = s2 - s3
s7 = s2 ^ s3
print(s4)
print(s5)
print(s6)
print(s7)