import os,random,string
from pathlib import Path
name = 'chem'
def save():
    
    path =  str(Path().absolute())+ "/"+ name
    try:
        os.mkdir(path) 
    except:
        pass
    openvar = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    filename = path+"/"+openvar+".json"
    o= open(filename,"w")
    o.write

save()