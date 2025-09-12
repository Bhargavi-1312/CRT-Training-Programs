# 13.WPP to check whether the user entered age is eglible to vote or not
age=int(input('enter the age:'))
if(age<=18):
    print('not eligible for vote')
else:
    print('eligible for vote')