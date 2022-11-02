def mountain_array(arr):
    i=1

    while i<len(arr) and arr[i] > arr[i-1]:
        i=i+1
    if i==1 or i>len(arr):
        return False
    while i<len(arr) and arr[i] < arr[i-1]:
        i=i+1

    return i==len(arr)

test1=[1,3,7,3,2] # true
test2=[4,2,7] #false
test3=[7,1,6] #false
test4=[8,9,5,4] #true

print(mountain_array(test1))
print(mountain_array(test2))
print(mountain_array(test3))
print(mountain_array(test4))