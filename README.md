# FitApp
#### Video Demo:  https://youtu.be/yh420tK9kVc
#### Description:

## What is FitApp?

FitApp, written in Python, is a voice recognizing command line program used to calculate your Body Mass Index,
Basal Metabolic Rate and Daily Calories to maintain your current weight. User only has to agree to a disclaimer,
Provide a name, height in inches, weight in pounds and age. Fitapp records the user's voice input, uses Google to
obtain the word and responds to the user.

The Disclaimer ensures that users do not use this program as any actual weight loss goal or anything else.
As a voice-activated automation, this program also prints what was said by the user on the command line. In order to ensure
that FitApp hears what was said, the user must wait until the command line prompts that it is listening. FitApp
will aska a question, then print "Yes or no?", "Height?", "Weight?" or "Age?". User input must be said during
these intervals for the program to hear it.

## Libraries used and their function:

### pyttsx3

I used pyttsx3 to output speech from text. This was useful to provide info and respond to user input in sync
with other libraries. This text-to-speech module although very useful, only allowed me to convert text and not
analyze speech.

### speech_recognition

Speech_recognition was used to obtain user input and voice which responds to questions from the program
and provides parameters. The Speech Recognition module obtains the speech which works with google to analyze
what was said with "recognize.google".

### word2number

Word2number was used for input of numbers as strings. It converts numbers as strings to numbers as floats.
So "thirty" needed to be converted to 30 before pluggin into formulas.


## Other Calculations

Google was used to recognize words in english. The user's input was plugged into formulas to calculate
values. Values were round from floats to whole numbers to provide more approximate values, and also to
provide a better user experience. Users were able to know their values whether they identified as female or male.

### Formulas used


Body Mass Index (BMI) = weight (lb) / (height (in))2 * 703

Women: Basal Metabolic Rate (BMR) = 655 + (4.35 x weight in pounds) + (4.7 x height in inches) – (4.7 x age in years)

Men: Basal Metabolic Rate (BMR) = 66 + (6.23 x weight in pounds) + (12.7 x height in inches) – (6.8 x age in years)

Maintenance calories = BMR * 1.2

"round" to round floats to integers.

## Issues

(1) Only understands integers for voice input.

Users would not be able to input a weight such as 170.5 or 170 1/2. Doing so would result in a program error.

(2) Issues with the while loops as they needed to repeat.

While loops might be either incorrect syntax or buggy, or the voice recognition is not advanced enough yet.

(3) Has to repeat name command when getting input from user.

Needs to hear the users name twice within the same input window.

(4) Timing issues for listening in to audio.

If audio input is not timed correctly, the program shuts down.

## Issues during installing and testing

(1) 'python' [0] argument in command line wouldn't work. 'python3' was needed.

(2) Issues installing pyttsx3 initially and pip.

## Feedback

I take all feedback as constructive. Feel free to contact me on your thoughts. Thank you.

