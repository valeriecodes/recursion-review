def search(arr, n):
    while len(arr) > 0:
        midpoint = len(arr) / 2
        if arr[midpoint] == n:
            return True
        elif arr[midpoint] > n:
            arr = arr[:midpoint]
        else:
            arr = arr[(midpoint + 1):]
    return False


print search([1, 2, 3, 4, 5], 1)
print search([1, 2, 3, 4, 5], 0)
