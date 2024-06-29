lines = ["Hi Parul\n\n", "I love you\n", "You're my Life.\n"]
with open('files/file2.txt', 'w') as file:
    file.writelines(lines)