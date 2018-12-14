c=1
while c<=3 :
    c += 1
    num = int(input('enter 4 digit pin number'))

    if num == 1234:
        print('lock successful')
        break
    elif c >= 4:
        print('Account is locked')
        break
    elif num != 1234:
        print('enter correct pin')


