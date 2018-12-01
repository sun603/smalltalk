from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Suit,Question
from random import randint
# Create your views here.
def index(request):
    return render(request, "index.html",) # {'home': 'active', 'chat': 'chat'})

@csrf_exempt
def Post(request):
    # while len(chat.conversation["general"])<2:
    #     chat.conversation["general"].append('initiate')
    if request.method == "POST":
        query = request.POST.get('msgbox', None)
        suit = int(request.POST.get('suit',None))
        qs = int(request.POST.get('qs',None))
        print(suit,qs)
        response = "Ok\n"
        if( suit == -1 and qs == -1):
            count = Suit.objects.count()
            random_suit = Suit.objects.all()[randint(0, count - 1)]
            response = random_suit.q1.question
            suit = random_suit.id
            qs = 1
        elif qs == 1 :
            used_suit = Suit.objects.get(pk=suit)
            qs = 2
            response = used_suit.q2.question
        elif qs == 2 :
            used_suit = Suit.objects.get(pk=suit)
            qs = 3
            response = used_suit.q3.question
        elif qs == 3 :
            qs = 4
            response = "Good job! Enough pratice for the day. Take a break."
        return JsonResponse({'response': response,'query': query,'suit':suit,'qs':qs})

    else:
        return HttpResponse('Request must be POST.')

'''
@csrf_exempt
def Post(request):
    while len(chat.conversation["general"])<2:
        chat.conversation["general"].append('initiate')
    if request.method == "POST":
        query = request.POST.get('msgbox', None)
        response = chat.respond(query)
        chat.conversation["general"].append('<br/>'.join(['ME: '+query, 'BOT: '+response]))
        if query.lower() in ['bye', 'quit', 'bbye', 'seeya', 'goodbye']:
            chat_saved = chat.conversation["general"][2:]
            response = response + '<br/>' + '<h3>Chat Summary:</h3><br/>' + '<br/><br/>'.join(chat_saved)
            chat.conversation["general"] = []
            return JsonResponse({'response': response, 'query': query})
        #c = Conversation(query=query, response=response)
        return JsonResponse({'response': response, 'query': query})
    else:
        return HttpResponse('Request must be POST.')
'''