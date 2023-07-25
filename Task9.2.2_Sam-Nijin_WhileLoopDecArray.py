unordered_array = list(map(int, input('Enter the elements with comma separated : ').split(',')))

def sort_array_with_while_loop(arr):
    
    n = len(arr)
    sorted = False

    while not sorted:
        
        sorted = True
        i = 0

        while i < n - 1:
            
            if arr[i] < arr[i + 1]:
                
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False
                
            i += 1
    return arr

ordered_array = sort_array_with_while_loop(unordered_array)

print("Sorted array:", ordered_array)
