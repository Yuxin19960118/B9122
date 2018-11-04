#author Yuxin Xia
import re
import numpy as np
#question 1
def convert(word):
    return word.replace('a','i')

#question 2 
def multi(n):
    if (not str(n).isdigit()) or ((int(n)<=0)):
        print ("not a positive interger")
        return -1
    for a in range(int(n)):
        for b in range(int(n)):
            print(str(a+1)+"*"+str(b+1)+"="+str((a+1)*(b+1)))
    return 0

#question 3
def sort(s):
    l=sorted(s.split(' '),key=lambda word:len(word))
    result=[]
    for i in range(len(l)):
        result.append((len(l[i]),l[i]))
    return result

#question 4
def count(file):
    l=file.replace('\n',' ').lower().split(' ')#l is a words list
    d={}#d is a dictionary to store words and frequency
    for word in l:
        if word in d.keys():
            d[word]+=1
        else:
            d[word]=1
    d=sorted(d.items(),key=lambda k:k[1],reverse=True)#d is a list
    for i in range(5):
        print(str(d[i][1])+' '+d[i][0])
    return d

#question 5
def reg_exp():
    #a 
    sa='^\d{4}-[0-1][0-9]-[0-3][0-9]$'
    #test for a
    ex=['2012-02-29','201-02-03','2012-25-30','2012-05-311','fwefe']
    for i in ex:
        if(re.search(sa,i)):
            print (i)
    #b
    sb='(^\d{5}$)|(^\d{5}-\d{4}$)'
    #test for b
    ex=['12343','234234-4234','43423-42342','43244-4324','23423-4234h','123456']
    for i in ex:
        if(re.search(sb,i)):
            print (i) 
    #c
    sc='^\w+@\w+\.com$'
    #test for c
    ex=['rwer@ewr.com','rwer2@ewr.com','dad@ewewecom','rwer@ewr.edu.com','rwer@ewr.comh','rwer@ewr..com']
    for i in ex:
        if(re.search(sc,i)):
            print (i)

#question 6
def same(a,b):
    l=(a==b)
    return [i for i in range(len(l)) if l[i]==True]   
    
    
#test for question 1
word='aeioua'
print(convert(word))
print()

#test for question 2
multi(4)
print()

#test for question 3
print(sort('this is a long sentence'))
print()

#test for question 4
fh = open('/Users/tiffanyxia/Downloads/hw1/question4.txt')
txt = fh.read()
count(txt)
fh.close()
print()
            
#test for question 5            
reg_exp()
print()

#test for question 6
a=np.array([1,2,3,2])
b=np.array([2,2,2,2])
print(same(a,b))

    

