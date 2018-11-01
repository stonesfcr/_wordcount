from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    fulltxt = request.GET['fulltext']
    wordlist = fulltxt.split()
    worddictionary = {}
    for w in wordlist:
        if w in worddictionary:
            worddictionary[w] += 1
        else:
            worddictionary[w] = 1
    sortedw = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltxt, 'count': len(wordlist), 'diccionario': sortedw})


def about(request):
    return render(request, 'about.html')
