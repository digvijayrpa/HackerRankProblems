to_upper = lambda text: text.upper()
print(to_upper('hello wolrd!!!'))

count_words = lambda sentence: len(sentence.split())
print(count_words("This is a sample sentence for python."))

reverse_words = lambda sentence: ' '.join(word[::-1] for word in sentence.split())
print(reverse_words("hello world"))
print(reverse_words("hello world")[::-1])
print("hello world"[::-1])

filter_words = lambda sentence, length: [word for word in sentence.split() if len(word) > length]
print(filter_words("I love parul because she is a good girl for me.", 3))

