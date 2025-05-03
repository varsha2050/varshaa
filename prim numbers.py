#input interval from user
start=int(input("enter the starting number of the interval:"))
end=int(input("enter the ending number of the interval:"))
print(f"prime numbers between {start}and{end}are:")
for num in range(start,end+1):
    if num <2:
        continue #skip numbers less than 2 (not prime)
    is_prime=rue
    for i in range(2,int (num**0.5)+1):
        if num%i==0:
            is_prime=false
            break#not a prime number
        if is_prime:
            print(num,end="")
            
                
