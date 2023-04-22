from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('chatbot',read_only=False,
                logic_adapters=[
                    {
                        'import_path':'chatterbot.logic.BestMatch',
                        'default_response':'Sorry, I dont know what that means',
                        'maximum_similarity_threashold':0.90

                    }])

list_to_train =[
    "Hey",
    "how are you feeling today?",
    "What's your name?",
    "I'm just a chatbot",
    "Happy",
    "Glad to hear that! Would you like to hear some music?",
    "Sure",
    "https://www.youtube.com/watch?v=o_v9MY_FMcw Here is some famous music by One direction Hope you enjoy :) ",
    "thanks",
    "how are you feeling now?",
    "Sad",
    "Would you like to hear a joke?",
    "why not",
    "Why did the invisible man turn down a job offer? Because he just couldn't see himself working there.",
    "haha",
    "how are you feeling now?",
    "Angry",
    "Let's cool you down..Try to picture a memory when you and your bestfriend had the best time together",
    "thanks",
    "how are you feeling now?",
    "Depressed",
    "It is okay to ask for help when you're struggling. If you want I can listen to you or try putting down your thoughts in Dear Diary section",
    "yeah",
    "how are you feeling now?",
]

list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

def index(request):
    return render(request,'chatbot/index.html')

def getResponse(request):
   userMessage = request.GET.get('userMessage')
   chatResponse = str(bot.get_response(userMessage))
   return HttpResponse(chatResponse)