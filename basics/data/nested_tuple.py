def steps ():
  likelihood =[("step 1", 50), ("step 2", 38) ,("step 3", 27),("step 4", 99) ,("step 5", 4)]
  return likelihood

def run ():
  likelihood = steps() 
  good_steps =[]
  bad_steps=[]
  for step in likelihood:
    if (step[1] >= 50):
      bad_steps.append(step)
    else:
      good_steps.append(step) 

  print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

run()