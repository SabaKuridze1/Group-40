def sort_by_a_count(my_list):
  def get_a_count(s):
    return s.lower().count('a')

  return sorted(my_list, key=get_a_count)

my_list = ["html", "is", "the", "worst", "web", "developing", "program", "ever"]
sorted_list = sort_by_a_count(my_list)
print(sorted_list)