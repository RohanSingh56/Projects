import smtplib
import speech_recognition as sr
import pyttsx3

from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
recognizer = sr.Recognizer()
email_list = {
    'Abhinav': 'abhinavbhatia2@gmail.com',
    'papa': 'bhatiamohan001@gmail.com',
    'Utkarsh': 'ux7432@gmail.com',
    'Jennifer': 'bhatiaritum@gmail.com'
}


def call():
    global text1, text2, text3
    with sr.Microphone() as source:
        engine.say('Clearing background noise...Please wait')
        engine.runAndWait()
        recognizer.adjust_for_ambient_noise(source, duration=1)
        engine.say("Send email to:")
        engine.runAndWait()
        recordedaudio1 = recognizer.listen(source)
        engine.say("Subject of the email:")
        engine.runAndWait()
        recordedaudio2 = recognizer.listen(source)
        engine.say("Text of the email:")
        engine.runAndWait()
        recordedaudio3 = recognizer.listen(source)
        print('Done recording')

    try:
        engine.say('Your message...Please wait')
        engine.runAndWait()
        text1 = recognizer.recognize_google(recordedaudio1, language='en-US')
        text2 = recognizer.recognize_google(recordedaudio2, language='en-US')
        text3 = recognizer.recognize_google(recordedaudio3, language='en-US')
        engine.say(text1)
        engine.runAndWait()
        engine.say(text2)
        engine.runAndWait()
        engine.say(text3)
        engine.runAndWait()

    except Exception as ex:
        print(ex)

    receiver = email_list[text1]
    engine.say(receiver)
    engine.runAndWait()
    send_email(receiver, text2, text3)
    engine.say('Hey pal your email is sent')
    engine.runAndWait()
    engine.say('Thanks')
    engine.runAndWait()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('', '')
    email = EmailMessage()
    email['From'] = ''
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


call()
engine.say('Do you want to send more email?')
engine.runAndWait()
with sr.Microphone() as source:
    engine.say('Clearing background noise...Please wait')
    engine.runAndWait()
    recognizer.adjust_for_ambient_noise(source, duration=1)
    engine.say("waiting for your message...")
    engine.runAndWait()
    recordedaudio = recognizer.listen(source)
    engine.say('Done recording')
    engine.runAndWait()

try:
    engine.say('Your message...Please wait')
    engine.runAndWait()
    text = recognizer.recognize_google(recordedaudio, language='en-US')
    engine.say(text)
    engine.runAndWait()

except Exception as ex:
    print(ex)
if 'no' in text:
    engine.say('Thanks for using the email assistant,have a nice day !')
    engine.runAndWait()
    exit()
else:
    while 'yes' in text:
        call()
        with sr.Microphone() as source:
            engine.say('Clearing background noise...Please wait')
            engine.runAndWait()
            recognizer.adjust_for_ambient_noise(source, duration=1)
            engine.say("waiting for your message...")
            engine.runAndWait()
            recordedaudio = recognizer.listen(source)
            engine.say('Done recording')
            engine.runAndWait()

        try:
            engine.say('Your message...Please wait')
            engine.runAndWait()
            text = recognizer.recognize_google(recordedaudio, language='en-US')
            engine.say(text)
            engine.runAndWait()

        except Exception as ex:
            print(ex)
        if 'no' in text:
            engine.say('Thanks for using the email assistant,have a nice day !')
            engine.runAndWait()
            exit()
