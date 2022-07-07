
import random
import string
from tkinter.messagebox import QUESTION

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

    def FormatSorter(self):
        if(self.formatType == 0): self.blanksformat()
        if(self.formatType == 1): self.longanswerformat()
        if(self.formatType == 2): self.multichoiceformat()
        if(self.formatType == 3): self.truefalseformat()
        if(self.formatType == 4): self.standardformat()
    def __formatinput__(self):
        rawdata = self.inputdata
        question = rawdata[0]
        answer = rawdata[1]
        return question,answer
    def blanksformat(self):
        q,a = self.formatinput()
        self.data = [q,a]
        q2= string(q)
        for items in a:
            q2.replace("-", string(items), 1)
        self.data = [q,q2]
        print(self.data)
    def longanswerformat(self):
        q,a = self.formatinput()
        q = string(q)
        a = string(a)
        self.data = [q,a.lower()]
    def multichoiceformat(self):
        q = self.inputdata
        a = q[len(q)-1]
        q.pop(len(q)-1)
        self.data = [q,a]
        
    def truefalseformat(self):
        q,a = self.formatinput()
        q = string(q)
        a = string(a) 
        a=a.lower() 
        if(a[0] == 't'):
            self.data = [q,True]
        else:
            self.data = [q,False]
    def standardformat(self):
        q,a = self.formatinput()
        q = string(q)
        a = string(a)
        self.data = [q,a] 

        


    


        

thing = cardclass(1,1,1,1,1,2,[,[]],3)
