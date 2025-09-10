def largestPermutation(k, arr):
    n = len(arr)
    val_to_idx = {val: idx for idx, val in enumerate(arr)}

    for i in range(n):
        if k == 0:  
            break
        target_val = n - i        
        if arr[i] != target_val:
            target_idx = val_to_idx[target_val]
            current_val_at_i = arr[i]
            arr[i], arr[target_idx] = arr[target_idx], arr[i]
            val_to_idx[current_val_at_i] = target_idx
            val_to_idx[target_val] = i
            k -= 1
    return arr
