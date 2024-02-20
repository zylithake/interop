#Z Akerele
# sources 1-https://stackoverflow.com/questions/2064184/remove-lines-from-a-textfile 2-https://stackoverflow.com/questions/2763750/how-to-replace-only-part-of-the-match-with-python-re-sub
#3-https://machinelearningtutorials.org/python-re-sub-function-performing-string-replacement-with-regular-expressions-with-examples/

import re
import codecs


def trim(my_str,sub):
  index=my_str.find(sub)
  if index !=-1 :
         return my_str[index:] 



fileData =  codecs.open('hvraw.txt', 'r', "utf-8")

rawData = fileData.read()

#trim header
cleanDat = trim(rawData,"</table>")

#replace Acts
actPat = re.compile(r"(\<h3\>)(ACT[ a-z]*)(\<\/h3\>)",re.IGNORECASE)
cleanDat = re.sub(actPat,r"== \2 ==",cleanDat)

#replace Scenes
scenePat = re.compile(r"\<h3\>(scene [ a-z]+)\.([\.a-z \-\']+)\<\/h3\>",re.IGNORECASE)
cleanDat = re.sub(scenePat,r"= \1 =\n{\2}",cleanDat)

#replace directions
dirPat = re.compile(r"\<i\>([ a-z]+)\<\/i\>",re.IGNORECASE)
cleanDat = re.sub(dirPat,r"[\1]",cleanDat)

#replace speech titles
speechPat = re.compile(r'\<a name="speech[0-9]+"\>\<b\>([ a-z]+)\<\/b\>\<\/a\>',re.IGNORECASE)
cleanDat = re.sub(speechPat,r"\1: ",cleanDat)

#replace lines
linePat = re.compile(r"\<a name=\"[0-9.]+\"\>([a-z ,.!?':;-]+)\<\/a\>",re.IGNORECASE)
cleanDat = re.sub(linePat,r"\t\1",cleanDat)


print(cleanDat)
