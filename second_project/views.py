from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html',{'hithere':'SO HERE IS A MESSAGE FOR YOU, Dear =)','hp':'our CEO wants to make you Director of the company'})
def eggs(request):
    return HttpResponse('<h1>MY EGGS ARE DELICIOUS</h1>')

def course(request):
    return render(request, 'index.html' )

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),key=operator.itemgetter(1),reverse= True)
    return render(request,'count.html',{'fulltext': fulltext,'counted':len(wordlist), 'sortedwords':sortedwords})
