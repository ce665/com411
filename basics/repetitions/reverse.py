print("what phrase do you see?")
phrase=input() 
print() 
for count in range(len(phrase)-1,-1,-1) :
  print(phrase[count],end:="") 
