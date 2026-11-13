# Lab Exercise 3: Frequency counter using dictionaries

text = input("Enter a sentence: ")

word_freq = {}
for word in text.lower().split():
    word_freq[word] = word_freq.get(word, 0) + 1

char_freq = {}
for ch in text.lower():
    if ch != " ":
        char_freq[ch] = char_freq.get(ch, 0) + 1

print("\nWord frequency:")
for word, count in word_freq.items():
    print(word, ":", count)

print("\nCharacter frequency:")
for ch, count in char_freq.items():
    print(ch, ":", count)
