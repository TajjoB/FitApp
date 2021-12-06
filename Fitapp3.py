# This is Fitapp using inches and pounds (imperial)
# Must be run with 'python3' and not 'python'

# Installed pyaudio and numpy
# Installed Flac
# Installed word2number to change numbers as words to numbers as floats

# Key issues:
# (1) Only understands integers
# (2) Issues with the while loops
# (3) Has to repeat each listen command when getting input from user
# (4) Timing issues for listening in to audio

import pyttsx3 # Output speech
import speech_recognition as sr # Input speech
from word2number import w2n # Changes numbers as words to numbers as floats for calculations

engine = pyttsx3.init()


# Set rate of speech
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 185)     # setting up new voice rate

def speak(audio): #define a speaking method
    engine.say(audio)
    engine.runAndWait()

def listen(): #define a listening method for greeting the user.

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.listen(source,timeout=2)
        audio = r.listen(source)

    try:
        print("Thinking...")
        global query
        query = r.recognize_google(audio, language = 'en-in')
        speak(f"I heard : {query}\n")

    except Exception as e: # In case AI doesnt understand name
        print(e)
        speak("I'm sorry, I didn't get that. I'll refer to you as User")
        query = "User"
        return



def greeting(): # Greets user!
    speak("What is your name?")
    username = listen()
    speak(f"Hello {query}!")
    print(f"Hello {query}!")
    



def finalAnswer(): # The final statement and calculation
    engine.say(f"Your BMI or Body Mass Index is {BMI}. If you're female, your Basal Metabolic Rate is {WBMR} and your maintenance calories are {WMC}. If you're male, your Basal Metabolic rate is {MBMR} and your maintenance calories are {MMC}. If you want to lose weight, ensure that the food you consume in each day is less than your maintenance calories, and, or do physical activity, so that your calories are less than your maintenance calories for the day. If you want to gain weight, ensure the food you consume in each day is more than your maintenance calories. Goodbye!")
    engine.runAndWait()
    print("") # Prints a new line.
    print (f"BMI = {BMI}")
    print (f"Female BMR is {WBMR}")
    print (f"Female Maintenance Calories is {WMC}")
    print (f"Male BMR is {MBMR}")
    print (f"Male Maintenance Calories is {MMC}")



# Disclaimer
speak("This program is strictly for an educational project and should not be used for any other purpose than that. The creator of this program takes no responsibility for any issues or problems arising from any other use. If you agree, say yes and I proceed, if not, say no and I terminate program.")

record = sr.Recognizer()
with sr.Microphone() as source:
    print("Yes or no?")
    disclaimAnswer = record.listen(source,timeout=2)

try:
    print("Analysing...")
    global googleAnswer
    googleAnswer = record.recognize_google(disclaimAnswer, language = 'en-in')
    googleAnswer = googleAnswer.lower()
    print(googleAnswer)

except sr.UnknownValueError():
    print("Error 0 with speech recognition!")
    quit()

if "no" or "yes" not in googleAnswer:
    while "no" or "yes" not in googleAnswer:
        speak("I did not understand. Please respond with the word yes or no.")
        record = sr.Recognizer()
        with sr.Microphone() as source:
            print("Yes or no?")
            disclaimAnswer = record.listen(source,timeout=2)

        try:
            print("Analysing...")
            googleAnswer = record.recognize_google(disclaimAnswer, language = 'en-in')
            googleAnswer = googleAnswer.lower()
            print (googleAnswer) #Checking Printout

        except sr.UnknownValueError():
            speak("Error 0 with speech recognition!")
            print("Error 0 with speech recognition!")
            quit()

        if "yes" or "no" in googleAnswer:
            break

# Terminate program if answer is 'no'
if "no" in googleAnswer:
    speak("I heard you say no. Yes, is required to proceeed. I'm sorry, I will have to terminate this program. Goodbye.")
    quit()
    # terminate program.

elif "yes" in googleAnswer:
    speak("I heard you say yes. Welcome to FitApp.")
    greeting()

else:
    speak("Critical error! Program terminated.")
    quit()




###################################################
# Get height
speak("What is your height in inches?")

record = sr.Recognizer()
with sr.Microphone() as source:
    print("Height?")
    heightAnswer = record.listen(source,timeout=2)

try:
    print("Analysing...")
    heightGoogle = record.recognize_google(heightAnswer, language = 'en-in')
    heightGoogle = heightGoogle.lower()
    heightGoogle = w2n.word_to_num(heightGoogle)
    print(heightGoogle)

except sr.UnknownValueError():
    print("Error 1 with speech recognition!")
    quit()

while heightGoogle != float or int:
    speak("Please enter your height with only a number in inches.")

    record = sr.Recognizer()
    with sr.Microphone() as source:
        print("Height?")
        heightAnswer = record.listen(source,timeout=2)

    try:
        print("Analysing...")
        heightGoogle = record.recognize_google(heightAnswer, language = 'en-in')
        heightGoogle = heightGoogle.lower()
        heightGoogle = w2n.word_to_num(heightGoogle)
        print(heightGoogle)

    except sr.UnknownValueError():
        print("Error 1 with speech recognition!")
        quit()
    if heightGoogle == float or int:
        break
#################################################
# Get Weight
speak("What is your weight in pounds?")

record = sr.Recognizer()
with sr.Microphone() as source:
    print("Weight?")
    weightAnswer = record.listen(source,timeout=2)

try:
    print("Analysing...")
    weightGoogle = record.recognize_google(weightAnswer, language = 'en-in')
    weightGoogle = weightGoogle.lower()
    weightGoogle = w2n.word_to_num(weightGoogle)
    print(weightGoogle)

except sr.UnknownValueError():
    print("Error 2 with speech recognition!")
    quit()

while weightGoogle != float or int:
    speak("Please enter your weight in pounds.")

    record = sr.Recognizer()
    with sr.Microphone() as source:
        print("Weight?")
        weightAnswer = record.listen(source,timeout=2)

    try:
        print("Analysing...")
        weightGoogle = record.recognize_google(weightAnswer, language = 'en-in')
        weightGoogle = weightGoogle.lower()
        weightGoogle = w2n.word_to_num(weightGoogle)
        print(weightGoogle)

    except sr.UnknownValueError():
        print("Error 2 with speech recognition!")
        quit()
    if weightGoogle == float or int:
        break

###################################################
# Get Age
speak("What is your age?")


record = sr.Recognizer()
with sr.Microphone() as source:
    print("Age?")
    ageAnswer = record.listen(source,timeout=2)

try:
    print("Analysing...")
    ageGoogle = record.recognize_google(ageAnswer, language = 'en-in')
    ageGoogle = ageGoogle.lower()
    ageGoogle = w2n.word_to_num(ageGoogle)
    print(ageGoogle)

except sr.UnknownValueError():
    print("Error 3 with speech recognition!")
    quit()

while ageGoogle != float or int:
    speak("Please enter your age.")

    record = sr.Recognizer()
    with sr.Microphone() as source:
        print("Age?")
        ageAnswer = record.listen(source,timeout=2)

    try:
        print("Analysing...")
        ageGoogle = record.recognize_google(ageAnswer, language = 'en-in')
        ageGoogle = ageGoogle.lower()
        ageGoogle = w2n.word_to_num(ageGoogle)
        print(ageGoogle)

    except sr.UnknownValueError():
        print("Error 3 with speech recognition!")
        quit()
    if ageGoogle == float or int:
        break
###################################################


###################################################

# Calculate BMI and other values
BMI = (weightGoogle/(heightGoogle * heightGoogle)) * 703

WBMR = 655 + (4.35 * weightGoogle) + (4.7 * heightGoogle) - (4.7 * ageGoogle)

MBMR = 66 + (6.23 * weightGoogle) + (12.7 * heightGoogle) - (6.8 * ageGoogle)

WMC = WBMR * 1.2

MMC = MBMR * 1.2

BMI = round(BMI)
WBMR = round(WBMR)
MBMR = round(MBMR)
WMC = round(WMC)
MMC = round(MMC)

finalAnswer()

quit()

# Metric:

# BMI = weight (kg) / (height (m)])2
# BMR basal metabolic rate = Women: BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (years) - 161
# BMR basal metabolic rate = Men: BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age (years) + 5
# Maintenance calories = BMR * 1.2

# Imperial:

# BMI = weight (lb) / (height (in))2 * 703
# Women: BMR = 655 + (4.35 x weight in pounds) + (4.7 x height in inches) – (4.7 x age in years)
# Men: BMR = 66 + (6.23 x weight in pounds) + (12.7 x height in inches) – (6.8 x age in years)