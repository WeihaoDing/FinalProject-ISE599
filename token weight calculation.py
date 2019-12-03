import json
import re
import nltk
import math
def main():
    fin = open("reviews_Digital_Music_2.csv", "r")
    line = fin.readline()
    fout=open("reviews_Digital_Music_Text.csv","a")
    #, reviewerName
    #fout.write("reviewerID, reviewText\n")
    L=[]
    tok=[]
    v=[]
    i=0
    line=fin.readline()
    while line:
        #print(line)
        s=line.split(",")
        #+"".join(str(s["reviewerName"]))+","
        #print(s["reviewerID"])
        str_=s[5]
        #print(str_)
        #pause
        str_=str_.replace("&quot","")
        str_=re.sub("[^a-zA-Z\s]+","",str_)#1. unify string
        str_=str_.replace("  "," ")#2. remove unnecessary spacing
        str_=str_.lower()#3. consistent casing
        tokens=str_.split(" ")#4. word tokenization
        freq=nltk.FreqDist(tokens)
        temp1=[]
        temp2=[]
        for key,val in freq.items():
            temp1.append(key)
            temp2.append(val)
            if key not in L:
                L.append(key)
        tok.append(temp1)
        v.append(temp2)
        #print (str(key) + ':' + str(val))
        #pause()
        #stemp=str_+"\n"#"".join(str(s["reviewerID"]).replace(",",""))+","+"".join(str(s["asin"]).replace(",",""))+","+"".join(str(s["helpful"]).replace(",",""))+","+"".join(str(s["reviewText"]).replace(",",""))+","+"".join(str(s["overall"]).replace(",",""))+","+"".join(str(s["summary"]).replace(",",""))+","+"".join(str(s["unixReviewTime"]).replace(",",""))+","+"".join(str(s["reviewTime"]).replace(",",""))+"\n"
        #fout.write(stemp)
        i=i+1
        line = fin.readline()
        print(i)
        #pause
    maxi=i
    strout=""
    for x in L:
        strout=strout+x+","
    strout=strout[0:-1]
    fout.write(strout+"\n")
    for i in range(0,maxi):
        strout=""
        for x in L:
            score=0
            if x in tok[i]:
                score=v[i][tok[i].index(x)]
            score=math.log(1+score,2)
            strout=strout+str(score)+","
        strout=strout[0:-1]
        fout.write(strout+"\n")
        print(i)

    fin.close()
    fout.close()
    return

if __name__=="__main__":
    main()