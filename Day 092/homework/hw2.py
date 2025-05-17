def sort_by_vowel_count(my_list):
  def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
      if char in vowels:
        count += 1
    return count

  return sorted(my_list, key=count_vowels, reverse=True)

my_list = ["asdasd", "aaaaaaaaaiioooe", "rqwtp", "sabaiaia", "abgdevztr"]
sorted_list = sort_by_vowel_count(my_list)
print(sorted_list)