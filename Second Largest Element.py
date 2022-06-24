def solve(n, arr):

    # to remove duplicate
    arr1=list(set(arr))

    # sort the list
    arr1.sort()

    return arr1[-2]
