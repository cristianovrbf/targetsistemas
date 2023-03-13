word = str(input("Digite uma palavra: "))
len = len(word)
i = 0
newWord = []
while(len > 0):
    len = len - 1
    newWord.append(word[len])
print(newWord)