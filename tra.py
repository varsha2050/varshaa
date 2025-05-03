#python program to print numbr in triangular form usingfor loop
rows=int(input("enter number of rows:"))
for i in range(rows,0,-1):
    print("\n")
for j in range(rows-i+1):
    print(i,"",end="")

