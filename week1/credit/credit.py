print('Number:',end='')
num = int(input())

pointer = 0
digit = 0
digitbuf = 0
sum = 0

while(num > 0):
    digitbuf = digit
    digit = num % 10
    pointer+=1
    if(pointer % 2 == 0):
        sum += (digit * 2) % 10 + (digit * 2) // 10
    else:
        sum += digit
    num = num // 10
print(sum)
cardtype = "INVALID"

if(sum % 10 == 0):
    if(digit == 3):
        if (pointer == 15 and (digitbuf == 4 or digitbuf == 7)):
            cardtype = "American Express"
            print(cardtype+'\n')
        else:
            print(cardtype+'\n')

    elif(digit == 4):
        if (pointer == 13 or pointer == 16):
            cardtype = "Visa"
            print(cardtype+'\n')
        else:
            print(cardtype+'\n')
        
    elif(digit == 5):
        if (pointer == 16 and (digitbuf > 0 and digitbuf < 6)):
            cardtype = "Mastercard"
            print(cardtype+'\n')
        else:
            print(cardtype+'\n')
    else:
        print(cardtype+'\n')
else:
    print(cardtype+'\n')
