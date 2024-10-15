# The commented imports are from attempts at reading emails
# import imaplib
# import email
# from email.header import decode_header
from transformers import pipeline
from huggingface_hub import InferenceClient

# Test input for Hugging Face
isThereEvent = "There is an event being announced."
eventQ = "What is the event?"
hostQ = "Who hosts the event?"
dayQ = "What day is the event"
timeQ = "At what time will the event occur?"
message = "PandaHat Society invites you to the 18th Hackathon thursday at 11am." # Event should be detected
noEvent = "There will be no chemistry test this sunday at 6:00pm." # No event should be detected
# This class represents the user and uses their info to access email information
# TODO: Add necessary login info for all services to be searched
# TODO: Add the functionality for reading emails, going through moodle, displaying with tkinter (or alternatives) and correctly process task complexity
# TODO: services (Gmail, Outlook, Moodle, Etc.)
class User:
    name = ""
    email = ""
    password = ""
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    # *GETTERS*
    def getName(self):
        return self.name
    def getEmail(self):
        return self.email
    def getPassword(self):
        return self.password
    
    # *SETTERS*
    def setName(self, name):
        self.name = name
    def setEmail(self, email):
        self.email = email
    def setPassword(self, password):
        self.password = password

def makeUser():
    # Take in credentials
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    return User(name, email, password)

# **Go through emails and save information**
# TODO: For testing, print sender and title
# TODO: Make similar functions for traversing info from the different services
def readEmails(user):
    pass

# **Using Hugging Face API analyze the email info**
# TODO: Experiment and learn how to implement correctly
def summarizeEmails():
    pass

# **For now this function will simply print the info, later display with tkinter**
# TODO: Learn about tkinter and how to use it, explore visually appealing alternatives for views
def displayInfo():
    pass

# **This function is the one that will later be used to analyze task complexities, where the AI action happens**
# TODO: Research the parameters and read documentation for the API
def testSummarizer():
    file = open("APIToken.txt", "r")
    token = file.readline()
    inference = InferenceClient(token = token)
    classifier = pipeline("text-classification", model = "roberta-large-mnli")
    eventRecognized = classifier(message + " " + isThereEvent)
    if eventRecognized[0]["label"] == "ENTAILMENT":
        print("Event detected.\nSummary:")
        event = inference.question_answering(question = eventQ, context = message)
        host = inference.question_answering(question = hostQ, context = message)
        day = inference.question_answering(question = dayQ, context = message)
        time = inference.question_answering(question = timeQ, context = message)
        eventSummary = event.answer + " on " + day.answer + " at " + time.answer + " by " + host.answer
        print(eventSummary)
    else:
        print("No event detected.")

# **Here we will put together all the segments of our code and later possibly move to different files
def main():
    # user1 = makeUser()
    # readEmails(user1)
    # displayInfo()
    testSummarizer()

main()
