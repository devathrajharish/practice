def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
# Driver program
A = [6, 5, 4, 9]
  
# Print required result
print(isMonotonic(A))