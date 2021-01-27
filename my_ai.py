import pyttsx3  # for text to speech
import speech_recognition  # for recognition of speech
import wikipedia  # for wikipedia summary
import webbrowser  # for working with web browsers
from datetime import *  # for time related stuffs
from time import sleep  # for sleep function

message = ''  # would be the message to be spoke
username = ''  # to remember the username
command = ''  # would be the command taken from user
summary = ''  # would be summary of search

# declaring variables related time
today = datetime.today()  # current time
date = today.strftime('%d')  # current date
month = today.strftime('%b')  # current month
day = today.strftime('%w')  # current day
hour = today.strftime('%H')  # current hour, should be on 24 hour format
minutes = today.strftime('%M')  # current minutes
seconds = today.strftime('%S')  # current seconds
am_pm = today.strftime('%p')  # am/pm

# initializing engine
engine = pyttsx3.init()
# engine.say('Hello World')
engine.runAndWait()

# recognizer
recognizer = speech_recognition.Recognizer()  # recognizer
microphone = speech_recognition.Microphone()  # microphone


# methods :
def say(sub):
    engine.say(sub)
    engine.runAndWait()


# noinspection PyChainedComparisons
def greet():
    if hour >= str(0) and hour <= str(12):
        say('good morning')
    elif hour >= str(13) and hour <= str(15):
        say('good afternoon')
    elif hour >= str(16) and hour <= str(20):
        say('good evening')
    else:
        # say("It's too late night sir, will talk tomorrow")
        # return
        pass
    sleep(0.3)
    say('I am an artificial bot, i am designed by master Rakshit, please tell me how might i help you')


if __name__ == '__main__':
    # greet()
    if hour >= str(22):
        # if time is greater than 10:00 pm, then exit
        sleep(0.3)
        say('I am tired, will talk later')
        say('Thank you for giving your precious time to me, i hope we will talk again, will meet soon, Bye')
        exit()

    while command != 'exit':
        # taking command
        with microphone as source:
            print('listening...')  # telling the user that microphone is listening
            recognizer.pause_threshold = 0.9  # waits for 0.9 seconds
            audio = recognizer.listen(source)
        # noinspection PyBroadException
        try:
            # recognizing
            print('recognizing...')
            sleep(0.1)
            command = recognizer.recognize_google(audio, language='en-in')
            print(f'command taken : {str(command).lower()}')
        except Exception as e:
            # if unable to recognize then:
            print('can you say that again please')

        # command should be in lower or upper case
        # defining choices :
        print('replying....')
        if command.lower() == 'exit':
            # if command taken from user is 'exit', then:
            say('Thank you for giving your precious time to me, i hope we will talk again, will meet soon, Bye')
            break  # terminates the infinite loop
        elif command.lower() == 'what is your name':
            # if command is 'what is your name' :
            say("well, i don't have a name till, my work is to win heart by my work not by my name")
        elif command.lower() == 'who are you':
            # if command is 'who are you'
            say('i am an artificial bot, i am designed by master Rakshit, my work is to help you out, kindly tell me '
                'how might i help you')
        elif 'how are you' in command.lower():
            # if command is 'how are you':
            say('I am fine as always, doing my work everytime, how about you')
        elif 'i am fine too' in command.lower():
            # connected with upper cae
            say('glad to hear')
        elif command.lower().startswith('hello'):
            # if command is starting with 'hello':
            greet()
        elif command.lower().startswith('I am'):
            # if user told his/her name using 'i am':
            username = command[5:].lower()  # remember the name
            print(f'username : {username}')
            say(f'hello {username}, you have such a wonderful name, i like it')
        elif command.startswith('my name is'):
            # name...
            username = command[11:].lower()
            print(username)
            say(f'hello {username}, you have such a wonderful name, i like it')
        elif 'tell me the time' in command.lower():
            # tells current time
            say(f'the time is {hour} hours and {minutes} minutes')
        elif 'what is the day today' in command.lower():
            # tells current day
            say(f'today is {day}')
        elif 'what is the date today' in command.lower():
            # tells current date
            say(f'today is {date} {month}')
        elif 'open google' in command.lower():
            # opens google
            say('opening google...')
            webbrowser.open_new_tab('google.com')
        elif 'open youtube' in command.lower():
            # opens youtube
            say('opening youtube...')
            webbrowser.open_new_tab('youtube.com')
        elif 'open github' in command.lower():
            # opens github
            say('opening github...')
            webbrowser.open_new_tab('github.com')
        elif 'open bing' in command.lower():
            # opens bing
            say('opening bing...')
            webbrowser.open_new_tab('bing.com')
        elif 'search' in command.lower():
            # searches the words after 'search'
            say('searching on wikipedia...')
            summary = wikipedia.summary(command.lower())
            # webbrowser.open_new_tab(wikipedia.summary(command))
            say(summary)
        else:
            # if no command matches, then :
            say('sorry, i did not got your command well, can you say that again please')
