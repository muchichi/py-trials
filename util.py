#Never odd or even

def main():
    #print('Palindroms')
    check_palindromes('Never Odd or Even')
    check_palindromes('Madam, I''m Adam')

def clean_text(text):
    pal = text.lower()
    punctuations = [' ',',','!','?',';','.','e']
    for x in list(punctuations):
        pal.replace(x,'')
    

def check_palindromes(pal):   
    mid,half,rest = 0,'',''
    x = int(len(pal))
    if(x%2 > 0):
        mid = (x//2) - 1
    else:        
        mid = (x//2)
          
    half = pal[:mid]
    rest = pal[mid:x][::-1]
    print('First part \t\t: \'{}\' Second part\t\t: \'{}\''.format(half,rest))
    print(half.replace(' ','') == rest.replace(' ',''))
    
if __name__=='__main__': main()
    
