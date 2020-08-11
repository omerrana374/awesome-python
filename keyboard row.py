class Solution:
    def findWords(self, words):
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'        
        oneRowWords = []
        for word in words:
            if all(letter in row1 for letter in word.lower()):
                oneRowWords.append(word)
            elif all(letter in row2 for letter in word.lower()):
                oneRowWords.append(word)
            elif all(letter in row3 for letter in word.lower()):
                oneRowWords.append(word)

        #return oneRowWords
        
        s1='QWERTYUIOP'
        s2='ASDFGHJKL'
        s3='ZXCVBNM'
        j=0
        arr=[]
        #count1=count2=count3=0
        
        for k in range(len(words)):
         count1=count2=count3=0   
         for i in range (len(words[k])):
            if (words[k][i].upper() in s1):
                count1=count1+1
            if (words[k][i].upper() in s2):
                count2=count2+1
            if (words[k][i].upper() in s3):
                count3=count3+1  
         
         if(count1==len(words[k]) or count2==len(words[k]) or count3==len(words[k])):
             arr.append(words[k])
            
        return(arr)   
        #print(arr)  
        
        
        
    
    
s=Solution()
s.findWords(["abdfs","cccd","a","qwwewm"])    
