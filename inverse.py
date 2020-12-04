class card:
    def __init__(self, setCode):
        self.setCode = setCode
        self.isKnown = True
        self.enabled = True
        self.sortKey = -1
    
    def str1(self):
        output = "%s\\isnown=%s\n" %(self.setCode, str(self.isKnown).lower())
        output += "%s\\enabled=%s\n" %(self.setCode, str(self.enabled).lower())
        if self.sortKey != -1:
            output += "%s\\sortkey=%s\n" %(self.setCode, str(self.sortKey))
        return output        
    
    def str2(self):
        output = "[%s]\n" %(self.setCode)
        output += "isnown=%s\n" %(str(self.isKnown).lower())
        output += "enabled=%s\n" %(str(self.enabled).lower())
        if self.sortKey != -1:
            output += "sortkey=%s\n" %(str(self.sortKey))
        return output        
    
f = open("cardDatabase.ini", "r")

cards = dict()
max = -1
sets = False

for l in f:
    line = l.split("\n")[0]
    print(line)
    if line == "[sets]":
        sets = True
    elif sets:
        setCode = line.split("\\")[0]
        
        entry = line.split("=")[0].split("\\")[1]
        value = line.split("=")[1]
          
        if not setCode in cards:
            cards[setCode] = card(setCode)
                
        if entry == "isknown":
            cards[setCode].isKnown = bool(value)
        elif entry == "enabled":
            cards[setCode].enabled = bool(value)
        elif entry == "sortkey":
            cards[setCode].sortKey = int(value)
              
            if max == -1 or cards[setCode].sortKey > max:
                max = cards[setCode].sortKey

f.close()

for c in cards:
    cards[c].sortKey = max - cards[c].sortKey + 1

f2 = open("cardDatabase.ini.new", "w+")
for c in cards:
    f2.write(cards[c].str2())
f2.write("[sets]\n")
for c in cards:
    f2.write(cards[c].str1())
f2.close()
