def likelihood (): 
  likelihoods =(50, 38, 27, 99, 4) 
  return min(likelihoods), max(likelihoods)


def run ():
  likelihoods=  likelihood () 
  print (f" Mnimum likelihood of falling :{likelihoods[0]}%") 
  print (f" Maximum likelihood of falling:{likelihoods[1]}%")

run() 