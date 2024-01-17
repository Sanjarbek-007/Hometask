a = int(input("Son kiriting :"))
lst = []
b = str(a)
a = str(a)
a = a[::-1]
a = int(a)


while a > 0:
    lst.append(a % 10)
    a //= 10

j = 0
for i in range(1,len(lst)):
    print(f"{(int(b[j:i])) * (10 ** (len(lst) - i))} + ",end="")
    j += 1
print(b[-1])