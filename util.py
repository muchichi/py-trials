#Never odd or even

def main():
    #print('Palindroms')
    check_palindromes('Never Odd or Even')
    #check_palindromes('Madam, I''m Adam')
    simple_pali('Never Odd or Even')

def clean_text(text):
    pal = text.lower().strip()
    #punctuations = [' ,,!,\',;,:]
    #pal.translate(None, str.punctuation)
    pal.replace(' ','')
    return pal
    

def check_palindromes(word):   
    pal = clean_text(word)
    mid,half,rest = 0,'',''
    x = int(len(pal))
    if(x%2 > 0):
        mid = (x//2) - 1
    else:        
        mid = (x//2)
          
    half = pal[:mid+1]
    rest = pal[mid:][::-1]
    print('First part: \'{}\' Second part: \'{}\''.format(half,rest))
    print(half.replace(' ','') == rest.replace(' ',''))
    
def simple_pali(word):
    pal = clean_text(word)
    if(pal[::].replace(' ','') == pal[::-1].replace(' ','')):
       print('We got palindrom >> {}'.format(pal[::]))
    else:
       print('Not at all >> {}'.format(pal[::-1].replace(' ','')))
        
        
        
    
if __name__=='__main__': main()
    
