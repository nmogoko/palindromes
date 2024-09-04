import string

words = open("wordlist.txt", "r")

palindromes = []

for word in words:
    word = word.translate(str.maketrans('', '', string.punctuation)).strip().replace(' ', '').lower()
    if word == word[::-1] and word != '':
        palindromes.append(word)
     
print(f"Number of palindromes: {len(palindromes)},\n Palindromes: {palindromes}")

