def search(arr, n):
  if arr == []:
    return False
  else:
    midpoint = len(arr) / 2
    if arr[midpoint] == n:
      return True
    elif arr[midpoint] > n:
      return search(arr[:midpoint], n)
    else:
      return search(arr[(midpoint + 1):], n)

print search([1, 2, 3, 4, 5], 1)
print search([1, 2, 3, 4, 5], 0)
