def introduction():
    print('''Input a sequence following this pattern:
    First, an integer:
        0: Indicates the start of a new sublist.
        1: Signals the end of all sublist inputs.
    If the first input is 0, the next input will be an integer x, representing the number of items in the sublist that follows.
    Then, x subsequent inputs will be the individual numbers to be included in that sublist.
    *This process will repeat until the code checker sends a 1.*''')


def createlist():
    L=[]    
    while True:
        I=int(input(""))
        if I==0:
            I=int(input("How many numbers in the set?"))
            S=set()
            for i in range(0,I):
                S.add(int(input("")))
            L.append(S)
        elif I==1:
             break        
    return L


def splitList(L):
    newlist=[]
    for i in range(0,len(L)):
        sublist=[]
        sublist.extend(L[i])       
        newlist.append(sublist)
    return newlist

    

introduction()
result=[{1,2,3},{4,5},{2,3,5}]
while True:
    result=createlist()
    print(result)
    a=input("Do you want to try again((Y)es/(N)o)?").upper()
    if  not (a == "YES" or a == "Y" ) :
        break
        

print("\ninput",result)
result2=splitList(result)
print("\nresult",result2)
