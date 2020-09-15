# I have created this file-vish
from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
  #  s='''<h1>Navigation Bar</h1> <a href="https://www.linkedin.com/in/vishal-jadhav-22928a174/">My Linked</a> <br><a href="https://www.codechef.com/">My Codechef</a>'''
  #  return HttpResponse(s)
def index(request):
    return render(request, 'index.html')
   # s='''<h1>Main Page</h1> <a href="http://127.0.0.1:8000/spaceremove">space remove</a><br><a href="http://127.0.0.1:8000/removepunc">removepunc</a><br><a href="http://127.0.0.1:8000/charcount">charcount</a><br><a href="http://127.0.0.1:8000/newlineremove">new line remove</a><br><a href="http://127.0.0.1:8000/capfirst">capfirst</a>'''
   # return HttpResponse(s)
   #return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremove=request.POST.get('newlineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')
    charcount=request.POST.get('charcount','off')

    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@$#%^&*_-'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params={'purpose':'Remove Punctuations','analyzed_text':analyzed}
        djtext=analyzed
    #s = '''<h1>removepunc</h1><a href="http://127.0.0.1:8000/">back to main</a>'''
       # return render(request,'analyze.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if newlineremove=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params={'purpose':'New line remove','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if extraspaceremove=="on":
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
                analyzed=analyzed+char
        params={'purpose':'Extra space remove','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)

    if charcount=="on":
        #analyzed=""
        cnt=0
        for char in djtext:
            if char!=" ":
                cnt=cnt+1

        params={'purpose':'character counter','analyzed_text':cnt}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    if(removepunc!="on" and newlineremove!="on" and extraspaceremove!="on" and fullcaps!="on"):
        return HttpResponse("Error")


    return render(request,'analyze.html',params)
#def capfirst(request):
    #s='''<h1>capfirst</h1><a href="http://127.0.0.1:8000/">back to main</a>'''
   # return HttpResponse(s)
#def removepunc(request):
   # djtext=request.GET.get('text','default')
   # print(djtext)
   # s = '''<h1>removepunc</h1><a href="http://127.0.0.1:8000/">back to main</a>'''
    #return HttpResponse("removepunc")
#def newlineremove(request):
    #s = '''<h1>newlineremove</h1><a href="http://127.0.0.1:8000/">back to main</a>'''
  #  return HttpResponse(s)
#def spaceremove(request):
 #   s = '''<h1>spaceremove</h1><a href="http://127.0.0.1:8000/">back to main</a>'''
   # return HttpResponse(s)
#def charcount(request):
    #s = '''<h1>charcount</h1><a href="http://127.0.0.1:8000/">back to main</a>'''
   # return HttpResponse(s)
