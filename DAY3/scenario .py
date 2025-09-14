#to organize the guess list
# to view the guess list
#to add the guess list
#to check the particular guest is attending the party
# to remove a guest from guest list
#to print the finalized guess list and exit

Guest_List=[]
while(True):
    print('----guest list menu-------')
    print("1.to view the guest list")
    print("2.to add the guest")
    print("3.to check the particular guest is attending the party")
    print("4.to remove the guest from guest list")
    print("5.to print the finalized guess list and exit")
    choice=int(input("enter your choice:"))
    if(choice==1):
        if(len(Guest_List)==0):
            print("guess list is empty")
        else:
            print(Guest_List)
        print()
    elif(choice==2):
        name=input("enter the name of the guest:")
        Guest_List.append(name)
        print("guest added successfully")
        print()
    elif(choice==3):
        name=input("enter the guest name to check the name is attending the party or not")
        if name in Guest_List:
            print(f"{name} is attending the party!")
        else:
            print(f"{name} is not attending the party!")
        print()
    elif(choice==4):
        name=input("enter the name of the guest who is not attending the party...")
        if name in Guest_List:
            Guest_List.remove(name)
            print(f"{name} is removed from the guess list")
        print()
    elif(choice==5):
        print("Finalized guess list and exit:")
        print()
        print(Guest_List)
        break                

    
