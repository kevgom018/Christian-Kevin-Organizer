import tkinter as tk
from tkinter import *
from tkinter import ttk

class OrganizerGUI(tk.Frame):
    def __init__(self, root, items = dict()):
        super().__init__(root)
        # Title Section
        self.titleFrame = ttk.Frame(root, padding = 10)
        self.titleFrame.grid(column = 0, row = 0)
        self.titleLabel = ttk.Label(self.titleFrame, text = "Testing GUI")
        self.titleLabel.grid(column = 0, row = 0)

        # Email Section
        self.emailFrame = ttk.Frame(root, padding = 10)
        self.emailFrame.grid(column = 0, row = 1)
        self.emailLabel = ttk.Label(self.emailFrame, text = "Enter your email:")
        self.emailLabel.grid(column = 0, row = 0)
        self.emailTextBox = ttk.Entry(self.emailFrame, name = "hello")
        self.emailTextBox.grid(column = 1, row = 0)

        # Password Section
        self.passFrame = ttk.Frame(root, padding = 10)
        self.passFrame.grid(column = 0, row = 2)
        self.passLabel = ttk.Label(self.passFrame, text = "Enter your password:")
        self.passLabel.grid(column = 0, row = 0)
        self.passTextBox = ttk.Entry(self.passFrame, show = "*")
        self.passTextBox.grid(column = 1, row = 0)

        # Quit Section
        self.quitButton = ttk.Button(text = "Quit", command = root.destroy)
        self.quitButton.grid(column = 0, row = 4)

        # List Section (Where the actual agenda will go)
        self.listItems = items
        self.agendaListBox = tk.Listbox(root, width = 40, justify = "center")
        self.agendaListBox.grid(column = 0, row = 3)
        self.showItems()
        

    # This method needs to be called in order to update display even at start
    def showItems(self):
        self.agendaListBox.delete(0, self.agendaListBox.size()) # Clears current display before updating
        index = 0
        for title in self.listItems:
            item = title + ": " + self.listItems[title]
            self.agendaListBox.insert(index, item)
            index += 1


    # Takes in a dictionary mapping items title to its content
    # Adds all items from dictionary to display
    def addItems(self, items):
        index = 0
        for title in items:
            self.listItems[title] = items[title]
        self.showItems()

    # Adds a single item to the display
    def addItem(self, title, content):
        self.listItems[title] = content
        self.showItems()
        
    # Removes a single item from the display
    def deleteItem(self, title):
        del self.listItems[title]
        self.showItems()

def main():
    root = tk.Tk()

    testingInfo = {"Kevin" : "Did it", "This" : "Rocks", "I" : "Gotta tell Chris"}
    mainGUI = OrganizerGUI(root, testingInfo)

    root.mainloop()

main()