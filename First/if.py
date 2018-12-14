data = [1, 'abc', 12463, 'ravi', 'teja', 564, 7894]
print(len(data))
last_index = len(data)-1
print(data[3:6])
name = data[3]+data[4]
print(name)
data[5] = 145
print(data)
del data[last_index]
print(data)
print(last_index)
a=round(len(data)/2)
print(data[a])

data2 = [2, 4, 6]
print(data*3)

str = 'python'
print(str[1:2])
data2 = data2.reverse()
print(data2)


a = [1, 5, 6, 8]
b = [1, 5, 6, 8]

for i in a :

    if len(a) != len(b):
        print("both lists are not matched")
        break
    elif a[i] != b[i] :
        print("elements in lists are not matched")
        break
    else :
        print("both lists are identical")

c = 'python'
i = len(c)
while i < 0 :
    print(c[i])
    i-=1