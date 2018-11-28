from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, "index.html",) # {'home': 'active', 'chat': 'chat'})

@csrf_exempt
def Post(request):
    # while len(chat.conversation["general"])<2:
    #     chat.conversation["general"].append('initiate')
    if request.method == "POST":
        query = request.POST.get('msgbox', None)
        print(query)
        response = "Ok\n"
        return JsonResponse({'response': response,'query': query})

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