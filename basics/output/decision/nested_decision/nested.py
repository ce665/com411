print("What cover does the book have?")

type=input()
if type == "soft" :
  print("Is the book perfect bound?")
  answer=input()
  if answer == "yes" :
    print("Soft cover; perfect bounds books are very popular")
  else:
    print("Soft covers with coils or stitches are great for short books")

else:
  print("Books with hard covers can be more expensive")
  