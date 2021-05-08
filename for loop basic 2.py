# #Biggie Size 
# def Biggie_Size (arr):
#     for i in range (0,len(arr)): 
#         if arr[i] > 0:
#             arr[i] = "big"
#     return arr      
# print (Biggie_Size ([4,2,-4,6]))

# #Count_Positives
# def Count_Positives(list):
#     count=0
#     for i in range (0,len(list)):
#         if list[i] > 0:
#             count=count+1
#             list[-1]=count
#     return list
# print (Count_Positives([1,-3,6]))

# #Sum Total 
# def Sum_Total (arr):
#     sum=0
#     for i in range (0,len(arr)):
#             sum=sum+arr[i]
#     return sum
# print (Sum_Total ([1,5,6]))

# #Average
# def Average (arr):
#     avg=0
#     sum=0
#     for i in range (0,len(arr)):
#         sum = sum + arr[i]
#         avg= sum/len(arr)
#     return avg
# print( Average ([1,2,3,4]))

# #Length
# def Length (arr):
#     for i in range (0,len(arr)):
#         return (len(arr))
# print (Length ([1,2,3]))

#Minimum
def Minimum (list):
    min=list[0]
    for i in range (0,len(list)):
        if list[i] < min:
            min=list[i]
    return min
print(Minimum ([1,2,3]))

#Maximum
def Maximum (list):
    max=list[0]
    for i in range (0,len(list)):
        if list[i] > max:
            max=list[i]
    return max
print(Maximum ([1,2,3]))

# #Ultimate Analysis
# def Ultimate_Analysis(arr):
#     dictionary = {
#         "sumtotal": sum(arr),
#         "average": sum(arr) / len(arr),
#         "minimum": min(arr),
#         "maximum": max(arr),
#         "length": len(arr),
#     }
#     return dictionary

# arr = [37,2,1,-9]
# print(Ultimate_Analysis(arr))  

# #Reverse List
# def Reverse_List(arr):
#     for i in range (int (len(arr)/2)):
#         arr[i],arr[len(arr)-1 -i] = arr[len(arr)-1 -i],arr[i]
#     return arr
# print(Reverse_List([37,2,1,-9]))