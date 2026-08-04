#Write a p2rogram to create patterns with stars using loops in Python.
rows=int(input("Enter a number of rows"))
for i in range(rows ,0, -1):
    for a in range(i,0, -1):
        print("⍟",end=" ")
    print()