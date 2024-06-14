def binary_search(array, shot): 
    start = 0
    end = len(array) - 1

    while start <= end:
        half = (start + end) // 2
        attempt = array[half]
        if attempt == shot:
            return half
        if attempt > shot:
            end = half - 1
        else:
            start = half + 1
    return None


array = [1, 3, 4, 5, 7, 8, 10]

shot = input("try a bumber:")
test = binary_search(array, int(shot))

print(test)