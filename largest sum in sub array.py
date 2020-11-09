import sys 
INT_MIN = -sys.maxsize
def maxSum(arr, n, k): 
      
    # Initialize result 
    max_sum = INT_MIN 
  
    # Consider all blocks  
    # starting with i. 
    for i in range(n - k + 1): 
        current_sum = 0
        for j in range(k): 
            current_sum = current_sum + arr[i + j] 
  
        # Update result if required. 
        max_sum = max(current_sum, max_sum ) 
  
    return max_sum 


if __name__ == "__main__":
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20] 
    k = 4
    n = len(arr) 
    print(maxSum(arr, n, k)) 
      