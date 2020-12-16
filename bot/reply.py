import random


class Reply:
    def __init__(self, message, frequency=100, searchType=0):
        self.message = message
        self.frequency = frequency

        # 0 -> contains, 1 -> startswith
        self.searchType = searchType

    def probabilityCheck(self):
        return True if self.frequency > random.randint(0,100) else False


class TextReply(Reply):
    def __init__(self, message, reply, frequency=100, searchType=0, inputType=0, userDict={}):
        super().__init__(message, frequency, searchType)
        self.reply = reply

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
    def getReply(self, message):
        finalReply = ""

        # Probability test to see if bot sends message
        if super().probabilityCheck():
            # Set default message
            finalReply = self.reply

            # Check for any special messages
            for currUser in self.userDict:
                if currUser == message.author.name:
                    finalReply = self.userDict[currUser]
                    break

            # Format based on inputType key
            if self.inputType == 1:
                finalReply = finalReply.format(message.author.name)
            elif self.inputType == 2:
                finalReply = finalReply.format(message.author.mention)
            elif self.inputType == 3:
                mention = '<@' + str(message.mentions[0].id) + '>' if len(message.mentions) > 0 else ""
                finalReply = finalReply.format(mention)

        return finalReply


class FuncReply(Reply):
    def __init__(self, message, func, frequency=100):
        super().__init__(message, frequency, 1)
        self.func = func

    # Returns correct reply given user
    def getReply(self, message):
        finalReply = ""

        # Probability test to see if bot sends message
        if super().probabilityCheck():
            paramList = message.content.replace(" > ", ">").split(">")
            finalReply = self.func(paramList)

        return finalReply
