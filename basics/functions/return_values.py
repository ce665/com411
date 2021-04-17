def sumweughts(weight_bot, weight_beep):
  tot_weight = weight_bot + weight_beep
  return tot_weight

def calc_avg_weight(weight_bot, weight_beep):
  avg_weight = (weight_bot + weight_beep) / 2
  return avg_weight

def run():
  print("what is the beep weight")
  size=int(input()) 
  print("What is bop weight")
  number=int(input()) 
  print("what would like to sum or average")
  action=input() 
  if (action == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
  elif (action == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
  else:
        print("I am not sure what you would like to do.")

run()