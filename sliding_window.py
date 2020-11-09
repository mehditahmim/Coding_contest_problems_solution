import sys 
INT_MIN = -sys.maxsize

def sliding_window(arr, n, k):
    
    summation = sum(arr[:k])
    max_sum = INT_MIN
    for i in range(n-k):
        previous_sum = summation
        summation = summation- arr[i] + arr[i+k]
        max_sum = max(summation,previous_sum)

    return max_sum    



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5] 
    k = 3
    n = len(arr) 
    print(sliding_window(arr, n, k))     

