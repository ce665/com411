print("How many lives cables i shoiuld avoid?")
cables=int(input())

cables_avoided=0
print()
while (cables_avoided<cables):
  print("Avoiding...", end="")
  cables_avoided=cables_avoided+1
  print("Done!", cables_avoided, "cables avoided.")