import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
list_fonetic = {row.letter:row.code for (index,row) in data.iterrows()}
word = input("Input a word ").upper()
code = [list_fonetic[letter] for letter in word]
print(code)