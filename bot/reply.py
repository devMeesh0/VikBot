import random

class Reply:
    def __init__(self, message, reply, frequency=100, searchType=0, inputType=0, userDict={}):
        self.message = message
        self.reply = reply
        self.frequency = frequency

        # 0 -> contains, 1 -> startswith
        self.searchType = searchType

        # 0 -> none, 1 -> author name, 2 -> author mention, 3 -> message mention
        self.inputType = inputType
        self.userDict = userDict

    # Adds a special reply
    def addSpecialReply(self, user, reply):
        self.userDict.update({user: reply})

    # Removes a special reply
    def removeSpecialReply(self, user):
        self.userDict.pop(user)

    # Returns correct reply given user
    def getReply(self, user):
        finalReply = ""

        # Probability test to see if bot sends message
        if self.frequency > random.randint(1, 100):
            # Set default message
            finalReply = self.reply

            # Check for any special messages
            for currUser in self.userDict:
                if currUser == user:
                    finalReply = self.userDict[currUser]
                    break

        return finalReply
