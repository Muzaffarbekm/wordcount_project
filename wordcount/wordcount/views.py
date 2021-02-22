from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request,'index.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for keyword in wordlist:
        if keyword in worddict:
            worddict[keyword] += 1
        else:
            worddict[keyword] = 1
    
    sorted_count = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'fulltext': fulltext, 'count': len(wordlist),'sorted_count': sorted_count})

def about(request):
    return render(request, 'about.html')