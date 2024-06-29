def count_words(text):
    word_counts = {}

    words = text.split()
    
    for word in words:
        word = word.lower()

        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

with open('files/file4.txt', 'r') as file:
    text = file.read()
    counter_words = count_words(text)
    for key in counter_words:
        print(f"{key}: {counter_words[key]}", end=' ')