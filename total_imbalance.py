from bisect import insort_left, bisect_left

def getTotalImbalance(arr):
    total_imbalance = 0
    
    for st_idx in range(len(arr)-1):
        curr_imb = 0
        curr_list = [arr[st_idx]]
        for en_idx in range(st_idx+1, len(arr)-1):
            insort_left(curr_list, arr[en_idx])
            idx = bisect_left(curr_list, arr[en_idx])
            
            if idx != 0 and idx+1 != len(curr_list) and curr_list[idx+1]-curr_list[idx-1] > 1:
                curr_imb -= 1
            if idx != 0 and curr_list[idx] - curr_list[idx-1] > 1:
                curr_imb += 1
            if idx != len(curr_list)-1 and curr_list[idx+1] - curr_list[idx] > 1:
                curr_imb += 1
            
            total_imbalance += curr_imb
    
    return total_imbalance

ans = getTotalImbalance([3,1,2])
print(ans)