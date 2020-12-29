def get_data():
    with open("AdventofCode2020Day2.txt", "rt") as AoCinput:
        lines = AoCinput.read().splitlines()
        return lines

entries = get_data()
entries [:5]


minimums=[]
maximums=[]
givenletters=[]
passwords=[]

for entry in entries:
    splitentry=entry.replace(":","").replace("-"," ").split(" ")
    minimums.append(splitentry[0])
    maximums.append(splitentry[1])
    givenletters.append(splitentry[2])
    passwords.append(splitentry[3])


#Part 1
numpassword=0

for password, givenletter, minimum, maximum in zip(passwords, givenletters, minimums, maximums):
    if password.count(givenletter)>=int(minimum) and password.count(givenletter)<=int(maximum): 
        numpassword += 1

print (numpassword)


#Part 2
numposition=0

for password, givenletter, minimum, maximum in zip(passwords, givenletters, minimums, maximums):
    if password[int(minimum)-1]!=password[int(maximum)-1] and (password[int(minimum)-1]==givenletter or password[int(maximum)-1]==givenletter):
        numposition += 1

print (numposition)




