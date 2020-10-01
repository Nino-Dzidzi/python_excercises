def gadmomeciricxvi(num):
  carieli_listi = []
  for i in range (1,num):
    if i % 3 == 0:
      carieli_listi.append(i)
    elif i % 5 == 0:
      carieli_listi.append(i)
  return carieli_listi


print (gadmomeciricxvi(num)) 
print(sum(gadmomeciricxvi(num)))