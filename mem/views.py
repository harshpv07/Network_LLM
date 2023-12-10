import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from google.cloud import dialogflow
from .models import ChatMessage

@csrf_exempt

def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        message = data.get('message', '')
        sender = data.get('sender', '')

        # Call Dialogflow API to get a response
        dialogflow_response = get_dialogflow_response(message)

        # Save user's message to the database
        ChatMessage.objects.create(sender=sender, message=message)

        return JsonResponse({'response': dialogflow_response})

    else:
        # Fetch chat history
        chat_history = ChatMessage.objects.all()
        return render(request, 'chat.html', {'chat_history': chat_history})

def get_dialogflow_response(message):
    # Implement Dialogflow API call here
    # Use the 'dialogflow' library or any HTTP client to send a request to Dialogflow
    # Return the response from Dialogflow
    # For simplicity, you can mock the response
    return f"Mocked response for: '{message}'"