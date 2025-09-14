size = int(input("Enter the size of the list: "))
char_list = []
for i in range(size):
    char = input(f"Enter an alphabetic character at index {i}: ")
    char_list.append(char)
print("User entered list:", char_list)
print("Sorted version of the list:", sorted(char_list))