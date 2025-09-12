#16.wpp to read an integer value as an input and print fizzbuzz if it is divisible by 3 and 5 print fizz 3 buzz 5

num=int(input('enter the number:'))
if(num%3==0 and num%5==0):
    print('fizzbuzz')
elif(num%3==0):
    print('fizz')
elif(num%5==0):
    print('buzz')