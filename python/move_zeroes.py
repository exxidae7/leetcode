# move all the zeros of an inorder array to the back of the array with out changing the order

# brute force

def move_zeros(arr):
    out = []
    for i in range(len(arr)):
        if arr[i] != 0:
            out.append(arr[i])

    if len(arr) == len(out):
        return out
    for i in range(len(arr) - len(out)):
        out.append(0)
    return out


arr = [0, 1, 0, 3, 12, 6]

rs = move_zeros(arr)
print(rs)

# optimized


def move_zeros_op(arr):
    j = 0
    for num in arr:
        if (num != 0):
            arr[j] = num
            j += 1
    for x in range(j, len(arr)):
        arr[x] = 0
    return arr
        
        
rs_op = move_zeros_op(arr)
print(rs_op)
