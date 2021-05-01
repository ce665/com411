def observed():
  observations = []

  for count in range(5):
    print("Please enter an observation:")
    observations.append(input())

  return observations

def remove_observations(observations):
  print("Do you wish to remove an observation (yes/no)?")
    response = input()

    if (response == "yes"):
      print("Please enter the observation you wish to remove")
      observation = input()
      observations.remove(observation)

def run():
  observations = observed()
  remove_observations(observations)

observations_set = set()