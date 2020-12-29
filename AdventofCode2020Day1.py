import itertools 

# store the input data into a variable 
# good practice guide in https://www.computerhope.com/issues/ch001721.htm
expenses = []
with open ('AdventofCode2020Day1.txt', 'rt') as AoCinput:   
    for expense in AoCinput:
        expenses.append(expense)
print(expenses)                                             



#make a list of all possible combinations of two values in sorted order from the input data
combsp1 = list(itertools.combinations(expenses, 2))
            
combsp1[:5]



#find ALL combinations which sum up to 2020
for comb in combsp1:
    if int(comb[0]) + int(comb[1]) == 2020:
        print ((comb[0]),(comb[1]), sep=' ')



#multiply combinations which sum up to 2020
for comb in combsp1:
    if int(comb[0]) + int(comb[1]) == 2020:
        print (int(comb[0])*int(comb[1]))



#repeat above but in a function and for combinations of 3
def main():
    combsp2 = list(itertools.combinations(expenses, 3))
    for comb in combsp2:
        if int(comb[0]) + int(comb[1]) + int(comb[2]) == 2020:
            print (int(comb[0])*int(comb[1])*int(comb[2]))

main()




