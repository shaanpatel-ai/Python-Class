#Part 1 -- 
# n=int(input("How many charters do you want to show"))
# file=open('solarsystem.txt','r')
# print(file.read(n))
# file.close()
# print( )
# #Part 2 -- all lines in list
# f=open('solarsystem.txt','r')
# lines = f.readlines()
# f.close()
# print("Total lines:",len(lines))
# for i in range(len(lines)):
#     print(i+1,"->",lines[i].strip())
# print( )
# #Part 3 -- Filter lines
# word=input("Skip lines starting with: ")
# file=open('solarsystem.txt','r')
# for line in file:
#     if line.startswith(word):
#         print("skip -. ",line.strip())
#     else:
#         print("keep ->", line.strip())
# file.close()
# print( )
#Part 4 -- Coppy odd lines to new file
file = open('solarsystem.txt','r')
lines=file.readlines()
file.close()
out=open('odd.txt','w')
for i in range(0,len(lines),2):
    out.write(lines[i])
out.close()
print("Odd lines saved to odd.txt")