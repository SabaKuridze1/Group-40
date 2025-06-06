def sort_by_three_frequency(numbers):
    def count_threes(n):
        count = 0
        for ch in str(n):
            if ch == '3':
                count += 1
        return count
    
    result = sorted(numbers, key=count_threes, reverse=True)
    return result





print(sort_by_three_frequency([333, 33333, 3, 3333333333333333, 3333333333333333333333, 33]))
