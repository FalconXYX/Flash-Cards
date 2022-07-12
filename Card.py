
import os,random,string
from pathlib import Path
import json

class cardclass():
    def __init__(self,x,y,l,w,color,formattype,data,guivariable):
        self.x= x
        self.y = y
        self.l = l
        self.w = w
        self.color = color
        self.formatType = formattype
        self.inputdata = data
        self.data = ""
        self.FormatSorter()
    def __init__(self,x,y,l,w,color,formattype,data,guivariable,deckname):
        self.x= x
        self.y = y
        self.l = l
        self.w = w
        self.color = color
        self.formatType = formattype
        self.inputdata = data
        self.data = ""
        self.name = deckname
        self.FormatSorter()
    def FormatSorter(self):
        if(self.formatType == 0): self.blanksformat()
        if(self.formatType == 1): self.longanswerformat()
        if(self.formatType == 2): self.multichoiceformat()
        if(self.formatType == 3): self.truefalseformat()
        if(self.formatType == 4): self.standardformat()
    def formatinput(self):
        rawdata = self.inputdata
        question = rawdata[0]
        answer = rawdata[1]
        return question,answer
    def blanksformat(self):
        q,a = self.formatinput()
        
        self.data = [q,a]
        q2= str(q)
        for items in a:
           q2 =  q2.replace("-", items, 1)
        self.data = [q,q2]
    def longanswerformat(self):
        q,a = self.formatinput()
        q = str(q)
        a = str(a)
        self.data = [q,a.lower()]
    def multichoiceformat(self):
        q = self.inputdata
        a = q[len(q)-1]
        q.pop(len(q)-1)
        self.data = [q,a]        
    def truefalseformat(self):
        q,a = self.formatinput()
        q = str(q)
        a = str(a) 
        a=a.lower() 
        if(a[0] == 't'):
            self.data = [q,True]
        else:
            self.data = [q,False]
    def standardformat(self):
        q,a = self.formatinput()
        q = str(q)
        a = str(a)
        self.data = [q,a] 
    def save(self):
        jsonvar =  json.loads('{ "data": self.data, "formattype":formattype,}')
        path =  str(Path().absolute())+ "/"+ self.name
        try:
            os.mkdir(path) 
        except:
            pass
        openvar = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
        filename = path+"/"+openvar+".json"
        o= open(filename,"w")
        o.write(jsonvar)


        


        

