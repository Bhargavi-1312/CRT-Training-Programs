size=int(input("Enter the size of the list: "))
num=[]
for i in range(size):
    n=int(input(f"Enter the element at {i} index: "))
    num.append(n)
print("User entered list is:", num)
print(num)
print("Size of the list is:", len(num))