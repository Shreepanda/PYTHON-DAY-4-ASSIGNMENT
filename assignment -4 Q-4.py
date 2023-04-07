num = int(input("Enter a number: "))
lsb = num % 10
while num >= 10:
    num //= 10
msb = num

print("LSB:", lsb)
print("MSB:", msb)
Enter a number: 1267899
LSB: 1
MSB: 9
