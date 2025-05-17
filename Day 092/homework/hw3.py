def sort_sentence_by_length(sentence):
  words = sentence.split()
  return sorted(words, key=len, reverse=True)

long_sentence = "დილასა ადრე მოვიდა იგი ნაზარდი სოსანი, ძოწეულითა მოსილი, პირად ბროლ-ბადახშოსანი პირ-ოქრო რიდე ეხვია, შვენოდა ქარქაშოსანი,მეფესა გასლვად აწვევდა, მოდგა თეთრ-ტაიჭოსანი."
sorted_words = sort_sentence_by_length(long_sentence)
print(sorted_words)