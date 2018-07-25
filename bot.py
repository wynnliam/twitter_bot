import json

"""
	Given the data set, we generate two dictionaries.
	The first maps each word in the data with a unique
	integer id. The second maps each unique id to its
	corresponding word. This way, we can quickly look up
	words and their numeric identifiers.

	PRECONDITIONS:
		dataset loaded in.

	POSTCONDITIONS:
		none

	ARGUMENTS:
		data - the dataset loaded in. Be sure to use
		dataset.json to load it in.

	RETURNS:
		Two dictionaries that map words to unique integer
		ids and vice-versa.
"""
def build_data_maps(data):
	word_to_id = dict()
	id_to_word = None
	unique_id = 0

	for datum in data:
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

f = open('dataset.json')
data = json.load(f)

w_to_i, i_to_w = build_data_maps(data)
print(w_to_i)
