def escape_by(plan):
  if (plan =="jumpin over"):
    print("We cannot escape that way! The boulder is too big!")
  elif (plan =="Running around") :
    print("we canot escape that way! The boulder is moving too fast")
  elif ( plan == "going deeper") :
    print (" That might just work. Lets go deeper")
  else :
    print("We cannot escape that way! The boulder is is in the way")

escape_by("jumpin over")
escape_by("Running around")
escape_by("going deeper")