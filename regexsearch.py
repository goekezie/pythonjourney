import re 
phonenum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenum.search('This is my number sirre 444-333-5655')
print(str(mo) + ' This all i could find ')
