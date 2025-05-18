myfile = open('myfile.txt','w+')
myfile.write("0 1 2 3 4 5 6 7  8 9 10")
myfile.seek(0)
mylist =[]
mylist2 = [letter for letter in range(1,13)]
print(mylist2)
for text in myfile.read():
    if not text.isspace():
        mylist.append(text)

print(mylist)

for text in mylist:
    print(text)
    print(type(text))
myfile.close()
list1 = [[2,3], [3,4], [6,8]]
for a,b in list1:
    print(a+b)
sum1 =0
for num in range(0,20,3):
    print(num)
    sum1+=num
print(sum1)
for item in zip(mylist, list1):
    print(item)
from random import randint
print(randint(1,199))
