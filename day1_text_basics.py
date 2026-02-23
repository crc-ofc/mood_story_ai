text = input("Enter your mood: ")

text = text.lower()
words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print("Words:", words)
print("Word Count:", word_count)

max_word = max(word_count, key=word_count.get)
print("Most frequent word is:", max_word)
