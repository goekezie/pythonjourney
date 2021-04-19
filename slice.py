spam = ['bans', 'bags', 'potato', 'yam']

def co(spam):
  rom = ""
  spams = spam[0:3]
  
  for i in spams:
    rom += str(i + ', ')
  
  rom += 'and ' + str(spam[len(spam)-1])

  return rom
print(co(spam))