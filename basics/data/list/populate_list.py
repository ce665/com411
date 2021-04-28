def direction ():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  directions = direction()
  for index in range(len(directions)):
    print(f"{index}: {directions}")
  answer= input() 
  return directions


def run():
  route=[]
  print("Working escape route")
  for count in range(5):
    route.append (menu())
    print(f"Escape route: {route}")

run()