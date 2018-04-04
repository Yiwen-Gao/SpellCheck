import pandas as pd

word = ""

def create_possible_words(test_word):
	global word
	word = test_word
	return transpose() + add_letter() + add_space() + remove_letter()


def transpose():
	global word
	possible_words = list()
	
	for i in range(0, len(word) - 1):
		if (i < len(word) - 2): 
			new_word = word[:i] + word[i + 1] + word[i] + word[i + 2:]
		else:
			new_word = word[:i] + word[i + 1] + word[i] 
		
		possible_words.append(new_word)
	
	return possible_words


def add_letter():
	global word
	possible_words = list()
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'k', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	
	for i in range(0, len(word) + 1):
		for j in range(0, len(alphabet)):
			new_word = word[:i] + alphabet[j] + word[i:]
			possible_words.append(new_word)

	return possible_words;


def add_space():
	global word
	possible_words = list()

	for i in range(1, len(word)):
		possible_words.append(word[:i])
		possible_words.append(word[i:])

	return possible_words


def remove_letter():
	global word
	possible_words = list()

	for i in range(0, len(word)):
		if (i < len(word) - 1):
			new_word = word[:i] + word[i + 1:]
		else:
			new_word = word[:i]
		possible_words.append(new_word)

	return possible_words

def get_from_my_dictionary():
	global word
	my_dictionary = pd.read_csv("my_dictionary.csv", delimiter = ",")
	original_words = my_dictionary["Original_Word"]
	corrected_words = my_dictionary["Corrected_Word"]

	for i in range(0, len(original_words)):
		if (word == original_words[i]):
			return corrected_words[i].split()

	return list()


