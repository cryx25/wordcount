from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
	return render(request,'homepage.html')

def word_count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			#Increase
			worddictionary[word] += 1
		else:
			#add to the dictionary
			worddictionary[word] = 1
	wordsort = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
	return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist), 'wordsort':wordsort})
def about_page(request):
	return render(request,'about.html')