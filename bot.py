import json

f = open('dataset.json')
data = json.load(f)

# Maps each word in the dataset to a unique number.
vocab = dict()
# Maps each unique number to a word in the dataset.
id_to_word_map = None
unique_id = 0

# Creates the vocab.
for datum in data:
	words = datum['text'].split(' ')
	for word in words:
		if word not in vocab:
			vocab[word] = unique_id
			unique_id += 1

vocab.update({"PADDING_VAL" : unique_id})
id_to_word_map = dict(zip(vocab.values(), vocab.keys()))
print(id_to_word_map)
