import pandas as pd
from possible_words import create_possible_words, get_from_my_dictionary

dictionary_file = pd.read_csv("dictionary.csv", delimiter = ",") #WILL THE CHANGES BE UPDATED IF I READ IN THE FILE IN THE BEGINNING? OR DO I HAVE TO REREAD IT EVERYTIME I UPDATE IT?
words = (dictionary_file["Word"]).tolist()
relative_frequency = (dictionary_file["Relative_Frequency"]).tolist()
user_created = (dictionary_file["User_Created"]).tolist()
times_selected = (dictionary_file["Times_Selected"]).tolist()
frequency = (dictionary_file["Frequency"]).tolist()

my_dictionary_file = pd.read_csv("my_dictionary.csv", delimiter = ",")
original_words = (my_dictionary_file["Original_Word"]).tolist()
corrected_words = (my_dictionary_file["Corrected_Word"]).tolist()

real_words = list()
corresponding_indexes = list()


def check_word(word):
	global real_words
	global corresponding_indexes

	if (check_in_dictionary(word) != -1):
		return True
	else:
		possible_words = create_possible_words(word)
		real_words = list()
		for i in range(0, len(possible_words)):
			index = check_in_dictionary(possible_words[i])
			if (index != -1):				
				real_words.append(possible_words[i]);
				corresponding_indexes.append(index)
	
	return real_words + get_from_my_dictionary();


def check_in_dictionary(word):
	global words

	for i in range(0, len(words)):
		if (word == words[i]):
			return i;
		
	return -1;


def update_corrections(original_word, corrected_word): 
	global real_words
	global corresponding_indexes
	global words
	global relative_frequency
	global user_created
	global times_selected
	global frequency
	in_suggestions = False;
	
	for i in range(0, len(real_words)):
		if (corrected_word == real_words[i]):
			in_suggestions = True;
			index = corresponding_indexes[i]
			
			user_created[index] = True
			times_selected[index] = (str) ((int) (times_selected[index]) + 1)
	
	if (not in_suggestions):
		index = check_in_dictionary(corrected_word)
		if (index == -1): 
			words.append(corrected_word)
			relative_frequency.append("")
			user_created.append(True)
			times_selected.append(1)
			frequency.append("")

		add_to_my_dictionary(original_word, corrected_word)

	dictionary_data = pd.DataFrame({"Word": words,
				"Relative_Frequency": relative_frequency,
				"User_Created": user_created,
				"Times_Selected": times_selected,
				"Frequency": frequency})

	data_file = pd.DataFrame(dictionary_data, columns = ["Word", "Relative_Frequency", "User_Created", "Times_Selected", "Frequency"])
	data_file.to_csv("dictionary.csv")


def add_to_my_dictionary(original_word, corrected_word):
	global original_words
	global corrected_words
	found = False;

	for i in range(0, len(original_words)):
		if (original_word == original_words[i]):
			found = True;
			if (check_unique(corrected_word, corrected_words[i])):
				corrected_words[i] = corrected_words[i] + " " + corrected_word

	if (not found):
		original_words.append(original_word)
		corrected_words.append(corrected_word)

	my_dictionary_data = pd.DataFrame({"Original_Word": original_words,
				"Corrected_Word": corrected_words})

	data_file = pd.DataFrame(my_dictionary_data, columns = ["Original_Word", "Corrected_Word"])
	data_file.to_csv("my_dictionary.csv")


def check_unique(corrected_word, corrections):
	global original_words
	global corrected_words

	corrections = corrections.split()
	for word in corrections:
		if (corrected_word == word):
			return False;

	return True;

