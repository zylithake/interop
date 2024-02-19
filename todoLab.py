#Z Akerele

#sources: 1:https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters  2:https://stackoverflow.com/questions/6576962/python-regular-expressions-return-true-false
#3: https://www.programiz.com/python-programming/regex 4:https://pythonexamples.org/python-re-sub/ 

import re
import codecs


#open files, import todo----------------------------------------------------------------------------------------------------------------------------------------------
data = codecs.open("todo.txt", 'r', "utf-8")
formattedData = codecs.open("formattedTodo.txt", 'w', "utf-8")


#regex to find: ------------------------------------------------------------------------------------------------------------------------------------------------

#name
namePat = re.compile(r"^(\w+[-]*\w+)\s\w*[.]*(\s*\w*)*", re.I) #only works if split into lines
#date
datePat = re.compile(r"\s(\d+)[/-](\d+)[/-](\d{4})", re.I)



#contact 
phonePat = re.compile(r"([(]?1?[)]?[(]?\d+[)]?[- ()]?[(]?\d{3}[)]?[- ]?\d{4})", re.I ) #phone numbers
emailPat = re.compile(r"(\w+@\w+[.]\w+)", re.I) #emails

#get data from file, prep lists-------------------------------------------------------------------------------------------------------------------------------------------------
rawData = data.read()
lineData = rawData.splitlines()
tasklist = []

cleanPat  = re.compile(r"([0-9,\\(-])",re.I)
#run regex on each line
#put regex results in dict-----------------------------------------------------------------------------------------------------------------------------------------

for line in lineData:
    lineNew = line

    #remove all data that is not task, store rest as task-----------------------------------------------------

    email = bool(re.search("@",line))
    
    # trim : name 
    lineNew = re.sub(namePat,'',lineNew)
    # trim : date
    lineNew = re.sub(datePat,'',lineNew)
    #trim: contact
    if email:
        lineNew = re.sub(emailPat,'',lineNew)
    else:
        lineNew = re.sub(phonePat,'',lineNew)
    
    #clean
    lineNew = re.sub(cleanPat,'',lineNew)
   
    #lineNew = task
        
  
   
    #put data into list of dicts
    if email:
        tasklist.append({'name':str((namePat.match(line)).group()),'date':str((datePat.findall(line))[0][2]) + '-' + str((datePat.findall(line))[0][1]) + '-' +str((datePat.findall(line))[0][0]), 'contact':str((emailPat.findall(line))[0]),'task':lineNew})
    else:
        tasklist.append({'name':str((namePat.match(line)).group()),'date':str((datePat.findall(line))[0][2]) + '-' + str((datePat.findall(line))[0][1]) + '-' +str((datePat.findall(line))[0][0]), 'contact':str((phonePat.findall(line))[0]),'task':lineNew})
    
  

        
#sort dict by date
Sortedlist = sorted(tasklist, key=lambda d: d['date']) 


#print formatted dict to txt file
for person in Sortedlist:
    formattedData.writelines('\n'+person['date'] + ': ' + person['task'] + '\n' + person['name'] + ',' + person['contact'] + '\n')












