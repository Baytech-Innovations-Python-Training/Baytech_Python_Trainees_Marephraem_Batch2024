unordered_array = list(map(int, input('Enter the elements with comma separated : ').split(',')))

def sort_array_with_for_loop(arr):
    
    n = len(arr)

    for i in range(n):
        
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

ordered_array=sort_array_with_for_loop(unordered_array)

print("ascending array:", ordered_array)
