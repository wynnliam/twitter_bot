import json

"""
	Given the data set, we generate two dictionaries.
	The first maps each word in the dataset with a unique
	integer id. The second maps each unique id to its
	corresponding word. This way, we can quickly look up
	words and their numeric identifiers.

	PRECONDITIONS:
		dataset loaded in.

	POSTCONDITIONS:
		none

	ARGUMENTS:
		dataset - the dataset loaded in. Be sure to use
		dataset.json to load it in.

	RETURNS:
		Two dictionaries that map words to unique integer
		ids and vice-versa.
"""
def build_dataset_dictionaries(dataset):
	word_to_id = dict()
	id_to_word = None
	unique_id = 0

	for datum in dataset:
		# The tweets JSON objects have the content stored under
		# 'text' key.
		words = datum['text'].split(' ')
		for word in words:
			if word not in word_to_id:
				word_to_id[word] = unique_id
				unique_id += 1

	# Add a unique word for "padding".
	word_to_id.update({"PADDING_VAL": unique_id})

	id_to_word = dict(zip(word_to_id.values(), word_to_id.keys()))
	return word_to_id, id_to_word

"""
	Scans each tweet and finds the "longest" one. We define "longest"
	meaning "most amount of words". This will then be used to build the
	traning data.

	PRECONDITIONS:
		Load dataset into memory from the dataset.json file. Also, there
		should be at least one tweet with one or more words in it.

	POSTCONDITIONS:
		None.

	ARGUMENTS:
		dataset - a dictionary form of the dataset.json file.

	RETURNS:
		The tweet with the most amount of words.
"""
def find_longest_tweet(dataset):
	curr_len = 0
	longest_len = 0

	for datum in dataset:
		curr_len = len(datum['text'].split(' '))
		if curr_len > longest_len:
			longest_len = curr_len

	return curr_len

f = open('dataset.json')
dataset = json.load(f)

w_to_i, i_to_w = build_dataset_dictionaries(dataset)
print(find_longest_tweet(dataset))
