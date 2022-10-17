#Swap UPPERCASE to lower and vise versa

def swap_case(s):
  pop = list(s)
  thing = ""
  print(pop)
  for x in pop:
    if x == x.upper():
      thing += x.lower()
      continue
    if x == x.lower():
      thing += x.upper()
      continue
    else:
      thing += x

  print(thing)
  return 1

swap_case("Hello Guys")