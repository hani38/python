#countdown
newlist = []
def Countdown (num):
    for i in range (num,-1,-1):
     newlist.append(i)
    return newlist
print(Countdown (5))

#print and return
def print_and_return (list):
    print (list[0])
    return list[1]
print ( print_and_return ([1,2]))

#First Plus Length
def First_Plus_Length (arr):
    firstvalue=arr[0]
    Length=len(arr)
    return  firstvalue + Length
print(First_Plus_Length ([1,3,2,5]))

#Values Greater than Second 
def Values_Greater_than_Second (list):
    newlist=[]
    secoundvalue=list[1]
    for i in range (0,len(list-1)):
        if (list(i) > secoundvalue):
            newlist.append(list[i])
        return newlist 
print (Values_Greater_than_Second ([1,3,5,9]))


#This Length, That Value
def ThisLength_ThatValue (size, Value):
    newlist=[]
    for i in range (size):
        newlist.append(Value)
    return newlist
print (ThisLength_ThatValue (4,7))











    
        