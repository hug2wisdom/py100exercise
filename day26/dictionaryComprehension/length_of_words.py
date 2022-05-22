sentence = "What is weather today do you know"
# transfer the string to list
sentence_list = sentence.split(" ")
# print(sentence_list)
word_count = {word: len(word) for word in sentence_list}
print(word_count)
