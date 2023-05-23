# Input card number
cardNumber = input("Number :")

# Verify if card number is valid
numSum = 0
for i in range(1, len(str(cardNumber)), 2):
    print("first i is :", cardNumber[::-1][i])
    tempVar = int(cardNumber[::-1][i]) * 2
    print("temp var 1 :", tempVar)
    if len(str(tempVar)) == 1:
        numSum += tempVar
    else:
        a = sum([int(x) for x in str(tempVar)])
        print("a is :", a)
        numSum += a
secondSum = 0
for i in range(0, len(str(cardNumber)), 2):
    print("second i is :", cardNumber[::-1][i])
    tempVar2 = int(cardNumber[::-1][i])
    print("temp var 2 :", tempVar2)
    if len(str(tempVar2)) == 1:
        secondSum += tempVar2
    else:
        a = sum([int(x) for x in str(tempVar2)])
        print("a2 is :", a)
        secondSum += a
print("numSum is :", numSum)
print("secondSum is :", secondSum)
finalSum = numSum + secondSum
b = [int(x) for x in str(finalSum)]

if b[1] == 0 and str(cardNumber)[0] == str(4) and (len(str(cardNumber)) == 13 or len(str(cardNumber)) == 16):
    print("VISA\n")
elif b[1] == 0 and (len(str(cardNumber)) == 15) and (str(cardNumber)[0:2] == str(34) or str(cardNumber)[0:2] == str(37)):
    print("AMEX\n")
elif b[1] == 0 and (len(str(cardNumber)) == 16) and (str(cardNumber)[0:2] == str(51) or str(cardNumber)[0:2] == str(52) or str(cardNumber)[0:2] == str(53) or str(cardNumber)[0:2] == str(54) or str(cardNumber)[0:2] == str(55)):
    print("MASTERCARD\n")
else:
    print("INVALID\n")
