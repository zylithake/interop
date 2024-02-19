import re
import codecs


fileData =  codecs.open('hvraw.txt', 'r', "utf-8")

rawData = fileData.read()
lineData = fileData.readlines()

print(rawData)