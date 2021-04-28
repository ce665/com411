def direction ():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def menu():
  print("Please select a direction:")
  directions = direction()
  for index in range(len(directions)):
    print(f"{index}: {directions[index]}")

def run():
  menu()

run()