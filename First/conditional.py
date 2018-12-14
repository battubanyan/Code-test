grades = ['A', 'B', 'C', 'D', 'E', 'S', 'FAIL']
number = input("enter marks")
marks = eval(number)
if type(marks) != int:
    print('plese enter valid input')
elif marks is 100:
    print ('your grade is'+ grades[5])
elif marks >= 90 and marks <= 99:
    print('your grade is'+ grades[0])
elif marks >= 80 and marks <= 89:
    print('your grade is'+ grades[1])
elif marks >=70 and marks <=79:
    print('your grade is'+ grades[2])
elif marks >=60 and marks <=69:
    print ('your grade is'+ grades[3])
elif marks >=50 and marks <=59:
    print ('your grade is'+ grades[4])
elif marks >=0 and marks <=50:
    print('you are'+grades[6])
else :
    print('not valid marks')

i=1
while i <= 10 :
    print(i)
    i+=1

b =[1, 2, 3, 4, 5, 6, 7, 8, 9]
a=1
for a in b :
    print(a)










