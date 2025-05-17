def sort_by_three_count(numbers):

  def count_threes(n):
    return str(n).count('3')

  return sorted(numbers, key=count_threes, reverse=True)

# მაგალითი
number_list = [132, 353, 123, 333, 521, 3, 931, 30]
sorted_list = sort_by_three_count(number_list)
print(sorted_list)