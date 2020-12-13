class Reply:
    def __init__(self, message, reply):
        self.message = message
        self.reply = reply
        self.userDict = {}

    def addSpecialReply(self, user, reply):
        self.userDict.update({user: reply})

    def removeSpecialReply(self, user):
        self.userDict.pop(user)

    def getReply(self, user):
        finalReply = self.reply

        for currUser in self.userDict:
            if currUser == user:
                finalReply = self.userDict[user]

        return finalReply


responseList = [Reply("guys", "and girls"), Reply("why", "because..."), Reply("yoink", "stop yoinken\' the wifi bumbo")]


def findReply(message, user):
    for obj in responseList:
        if obj.message == message:
            return obj.getReply(user)


print(findReply("-hello", "kgupta1542"))

responseList.append(Reply("-hello","Hello!"))
responseList[3].addSpecialReply("kgupta1542","shut up kanishk")
print(findReply("-hello", "kgupta1542"))

responseList[3].removeSpecialReply("kgupta1542")
print(findReply("-hello", "kgupta1542"))
print(findReply("why","fakeUser"))
