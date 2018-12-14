num = 25
l = 25 is num
print(l)
m = 25 is not num
print(m)

age = input("enter age")
if age is not int:
    print('plese enter integer value')
elif age >= 0 and age <= 18:
    print('you are minor')
elif age >= 18 and age <= 60:
    print('you are adult')
elif age > 60:
    print('you are senior citizen')
else:
    print('not valid age')

i = 1
while (i < 100):
    if i<2 :
        i+=1
        print(i)
    else :
        i+=2
        print(i)










