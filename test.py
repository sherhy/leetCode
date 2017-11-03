s = 'asdfksdjranarldkfj'

i = 8
j = 12
print( s[i:j+1])
print( s[j:i-1:-1])
print( i > 0 and s[i:j+1] != s[j:i-1:-1], i == 0 and s[i:j+1] != s[j::-1])