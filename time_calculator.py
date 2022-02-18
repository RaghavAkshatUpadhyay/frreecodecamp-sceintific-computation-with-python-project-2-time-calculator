def add_time(start, duration,dayname=None):
  arr=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
  arrr={"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
  amorpm=start[start.find(' '):]
  originalhrs=int(start[0:start.find(':')])
  originalmins=int(start[start.find(':')+1:start.find(" ")])
  updatehrs=int(duration[0:duration.find(':')])
  updatemins=int(duration[duration.find(':')+1:])
  newword=list()
  newword.append(originalhrs+updatehrs)
  newword.append(updatemins+originalmins)
  newword.append(int(0))
  if(newword[1]>60):
    newword[0]=newword[0]+1
    newword[1]=newword[1]-60

  if(amorpm == ' PM'):
        print("s")
        newword[0]=newword[0]+12
  if(newword[0]>24):
        newword[2]=round(newword[0]/24)
        
  newword[0]=newword[0]%24

  if(newword[0]==0):
        newword[0]=12
        newword.append(' AM') 
  elif(newword[0]<12):
        newword.append(' AM') 
  elif(newword[0]==12):
        newword.append(' PM')    
  elif(newword[0]>12):
        newword[0]=newword[0]-12
        newword.append(' PM') 
  

  if((len(str(newword[1])))==1):
        new_time=str(newword[0])+":0"+str(newword[1])+newword[3]
  else:
        new_time=str(newword[0])+":"+str(newword[1])+newword[3]
  
  if(dayname!=None):
    dayname=dayname.lower()
    x=int(newword[2]%7)
    x=x+int(arrr[dayname])
    if(x>=7):
      x=x%7
    day=arr[x]
    new_time=new_time+", "+day+" "
  else:
    new_time=new_time+" "  
   
  if(newword[2]==0):
        new_time=new_time+""
  elif(newword[2]==1): 
        new_time=new_time+"(next day)"
  elif(newword[2]>1):
        new_time=new_time+"("+str(newword[2])+" days later)"
  new_time=new_time.rstrip()
  return new_time
 
