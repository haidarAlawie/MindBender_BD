import re
def word_count():
	
	# load text
	text = open("Shakespeare.txt", "r")
	
	# turn text into a string
	text_to_string = " "
	for line in text:
		text_to_string= text_to_string + " " + line

	# get rid of all symbols using regex 
	text_only = re.sub(r'[^\w]', ' ', text_to_string)


	# split text into words
	split_text = text_only.split(" ")


	word_dictionary= {}

	for word in split_text:
		# check if the word is already added into dictionary

		if word.lower() in word_dictionary:
			# increment value 
			word_dictionary[word.lower()] = word_dictionary[word.lower()] +1
		# dont add if not a word
		elif word == "" :
			continue
		# add into dictionary if it isnt there and set value to 1 
		else:
			word_dictionary[word.lower()] = 1

	text.close()
	for i in word_dictionary:
		print (i, " ", word_dictionary[i])



word_count()





