string=input('enter the name:')
vowels,consonants=0,0
for ch in string.lower():
    if ch in 'aeiou':
        vowels+=1
    elif ch.isalpha():
        consonants+=1
print(f"count of vowels is :",{vowels})
print(f"count of consonants is :",{consonants})            