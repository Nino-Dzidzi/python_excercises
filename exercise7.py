a = input("Shemoiyvane teqsturi mnishvneloba: ")

def middle_element(sia):
  if len(sia) % 2 != 0:
    return sia[len(sia) // 2]
  else:
    return (sia[len(sia) // 2 - 1], sia[len(sia) //2])

x = middle_element(a.split (","))
print(x)