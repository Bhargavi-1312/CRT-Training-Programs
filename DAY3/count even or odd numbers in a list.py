a=[11,34,6,78,90,23]
even_count=sum(1 for num in a if num%2==0)
odd_count=sum(1 for num in a if num%2!=0)
print(f"even numbers count: {even_count}")
print(f"odd numbers count: {odd_count}")
