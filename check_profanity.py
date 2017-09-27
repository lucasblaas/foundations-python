import urllib

def read_text():
	quotes = open("/Users/lucblaas/Desktop/python-course/movie_quotes.txt")
	content_of_file = quotes.read()
	# print(content_of_file)
	quotes.close()

	check_profanity(content_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
	output = connection.read()
	# print(output)
	connection.close()

	if "true" in output:
		print "Profanity Alert!!"
	elif "false" in output:
		print "This document has no curse words!"
	else:
		print "Could not scan the document properly."		

read_text()	