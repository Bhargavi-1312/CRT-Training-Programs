# 12. WPP TO READ THE MONTH NUMBER AS A INPUT FROM THE USER AND PRINT THE RESPECTIVE NUMBER OF DAYS IN THAT PARTICULAR MONTH
m=int(input('enter the month number:'))
if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print('31 days')
elif(m==2):
    print('28 or 29 days')
elif(m==4 or m==6 or m==9 or m==11):
    print('30 days')
else:
    print('invalid')     