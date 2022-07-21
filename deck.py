import Card
import os,random,string
from pathlib import Path
import json
class deckclass():
    def __init__(self,x,y,guivariable,deckname,i):
        self.x= x
        self.y = y
        self.data = []
        self.indexdata = []
        self.length = 0
        self.guivariable = guivariable
        self.name = deckname
        self.path =  str(Path().absolute())+ "/"+ deckname+"/index.json"
        if(i ==1):
            o = open(self.path,"r")
            self.indexdata = json.load(o)
            self.indexdata = self.indexdata["array"]
            self.length = len(self.indexdata)
            self.data = []
            for item in self.indexdata:
                tempPath = str(Path().absolute())+ "/"+ deckname+"/"+item
                op = open(tempPath,"r")
                tempdata = json.load(op)
                self.length += 1
                self.data.append(Card.cardclass(0,0,0,0,(0,0,0),tempdata["FormatNum"],tempdata["Data"],guivariable,deckname))
                
            
        else:
            try:
                os.makedirs(str(Path().absolute())+ "/"+ deckname)
            except :
                pass
            o = open(self.path,"w")
            jsonvar =  {"array" : []}
            jsonvar = json.dumps(jsonvar, indent = 1)
            o.write(jsonvar)
            
            
        
   
        
    def addcard(self,card):
        self.length += 1
        temp = card.save()
        self.data.append(card)
        o = open(self.path,"w")
        self.indexdata.append(temp)
        o = open(self.path,"w")
        jsonvar =  {
        "array" : self.indexdata}
        jsonvar = json.dumps(jsonvar, indent = 1)
        o.write(jsonvar)

    def createcard(self,data,formatnum):
        self.length += 1
        temp = Card.cardclass(0,0,0,0,(0,0,0),formatnum,data,self.guivariable,self.name)
        self.data.append(temp)
        temp = temp.save()
        self.indexdata.append(temp)
        o = open(self.path,"w")
        jsonvar =  {
        "array" : self.indexdata}
        jsonvar = json.dumps(jsonvar, indent = 1)
        o.write(jsonvar)

    def removecard(self,card):
        self.length -= 1
        indexvalue = self.data.index(card)
        self.data.remove(card)
        self.indexdata.remove(self.indexdata[indexvalue])
        o = open(self.path,"w")
        jsonvar =  {
        "array" : self.indexdata}
        jsonvar = json.dumps(jsonvar, indent = 1)
        o.write(jsonvar)


test = deckclass(0,0,0,"test",1)
test.createcard(["What the most popular langauges","python","javascript","c++","java",2],2)
t = test.data[6]
        
print(t.data)

        
