def find_sum(arr): #in Algorithm 3 class from time 1hr.28min
    max_sum=current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)
        max_sum = max(max_sum, current_sum)
    return max_sum

sum_of_list = [1,2,-1,3,4,10,10,-10,-1]
print(find_sum(sum_of_list))