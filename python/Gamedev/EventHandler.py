from dataclasses import dataclass

@dataclass
class flag:
    timeSinceLast: int # int because it deals with number of frames since
    data: list # any required data which needs to be passed to the event handler
    activation_time: int # time to activation

class EventHandler:
    def __init__(self):
        self.flags = {}
        self.functionMap = { # print action is just an example
            "print": print
        }
    
    def performAction(self, ID, args):
        if not(ID in self.functionMap.keys()):
            return
        func = self.functionMap[ID]
        func(*args)
    
    def getTriggeredFlags(self):
        triggered = []
        for key in self.flags.keys():
            if self.flags[key].timeSinceLast == 0:
                triggered.append(key)
        return triggered

    def tick(self):
        for key in self.flags.keys():
            flag = self.flags[key]
            if flag.timeSinceLast == flag.activation_time:
                self.performAction(key, flag.data)
            flag.timeSinceLast += 1
    
    def getFlag(self, ID):
        return self.flags[ID]
    
    def triggerFlag(self, ID, data, activation_time = 0):
        self.flags[ID] = flag(0, data, activation_time)