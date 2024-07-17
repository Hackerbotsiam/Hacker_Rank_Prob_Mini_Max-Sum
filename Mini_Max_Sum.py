# Mini_Max_Sum

def miniMaxSum(arr):

    total_sum= sum(arr)# Here solve total sum of this array

    max_value= max(arr) # Find out maximum value of this array
    min_value= min(arr) # Find out minimum value of this array

    # Calculate maximum sum:

    max_sum= total_sum - min_value
    min_sum= total_sum - max_value

    # print out the result
    print(min_sum,max_sum)

arr= list(map(int,input().split()))
if len(arr)!=5:
    print("Error")
else:
    miniMaxSum(arr)

