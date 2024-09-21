# define services (Gmail, Outlook, Moodle, Etc.)

# The commented imports are from attempts at reading emails
# import imaplib
# import email
# from email.header import decode_header
from transformers import pipeline
from huggingface_hub import InferenceApi

# Test input for Hugging Face
question = "What is the capital of Belgium?"

# This class represents the user and uses their info to access email information
# TODO: Add necessary login info for all services to be searched
# TODO: Add the functionality for reading emails, going through moodle, displaying with tkinter (or alternatives) and correctly process task complexity
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

# **This function is the one that will later be used to analyze task complexities, where the AI action happens
# TODO: Research the parameters and read documentation for the API
def testSummarizer():
    file = open("kevinToken.txt", "r")
    token = file.readline()
    api = InferenceApi(repo_id = "gpt2", token = token)
    output = api(inputs = "What is the capital of Belgium?")
    print(output[0]["generated_text"])

# **Here we will put together all the segments of our code and later possibly move to different files
def main():
    user1 = makeUser()
    readEmails(user1)
    displayInfo()
    testSummarizer()

main()
