a = "[1, 2, 3, 4, 5, 6, 7, 8, 9]"
b = "['A', 'B', 'C', 'D', 'E', 'F', 'G']"
c = "['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']"

print(a)
print(b)
print(c)

print ('============================================================================================')

# list 1
def balik_list(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "]1, 2, 3, 4, 5, 6, 7, 8, 9["

print ("List yang sudah dibalik : ",end="")
print (balik_list(s))



# list 2
def balik_list(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "]'A', 'B', 'C', 'D', 'E', 'F', 'G'["

print ("List yang sudah dibalik : ",end="")
print (balik_list(s))

# list 3
def balik_list(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "]'isseM', 'zerauS', 'ohnituoC', 'elebmeD', 'citikaR'["

print ("List yang sudah dibalik : ",end="")
print (balik_list(s))