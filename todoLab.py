#Z Akerele

#sources: 1:https://stackoverflow.com/questions/24237524/how-to-split-a-python-string-on-new-line-characters  2:https://stackoverflow.com/questions/6576962/python-regular-expressions-return-true-false
#3: https://www.programiz.com/python-programming/regex 

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


#run regex on each line
#put regex results in dict-----------------------------------------------------------------------------------------------------------------------------------------

for line in lineData:
    print(line)
    email = bool(re.search("@",line))
    print("name  :  " + str((namePat.match(line)).group()))
    

    if email:
        tasklist.append({'name':str((namePat.match(line)).group()),'date':str((datePat.findall(line))[0][1]) + '-' + str((datePat.findall(line))[0][0]) + '-' +str((datePat.findall(line))[0][2]), 'contact':str((emailPat.findall(line))[0]),'task':''})
    else:
        tasklist.append({'name':str((namePat.match(line)).group()),'date':str((datePat.findall(line))[0][1]) + '-' + str((datePat.findall(line))[0][0]) + '-' +str((datePat.findall(line))[0][2]), 'contact':str((phonePat.findall(line))[0]),'task':''})

    
#remove all data that is not task, store rest as task

    
    






#sort dict by date



#output formatted dict to new file-------------------------------------------------------------------------------------------------------------------------------------

print(tasklist)


