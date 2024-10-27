# This is the class that represents tasks (i.e. homework, essays, projects, etc.)
class Task:
    title = ""
    description = ""
    dueDate = ""
    def __init__(self, title, description, dueDate):
        self.title = title
        self.description = description
        self.dueDate = dueDate

    # *GETTERS*
    def getTitle(self):
        return self.title
    
    def getDescription(self):
        return self.description
    
    def getDueDate(self):
        return self.dueDate
    
    # *SETTERS*
    def setTitle(self, title):
        self.title = title
    
    def setDescription(self, description):
        self.description = description
    
    def setDueDate(self, dueDate):
        self.dueDate = dueDate

# This class will represent events (i.e. tests, presentations, meetings, workshops, interviews)
class Event:
    type = ""
    title = ""
    host = ""
    date = ""
    def __init__(self, type, title, host, date):
        self.type = type
        self.title = title
        self.host = host
        self.date = date

    # *GETTERS*
    def getType(self):
        return self.type
    
    def getTitle(self):
        return self.title
    
    def getHost(self):
        return self.host
    
    def getDate(self):
        return self.date
    
    # *SETTERS*
    def setType(self, type):
        self.type = type
    
    def setTitle(self, title):
        self.title = title
    
    def setHost(self, host):
        self.host = host     

    def setDate(self, date):
        self.date = date

        