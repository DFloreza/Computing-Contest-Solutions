place = 1
x = 1
while 0 < x <= 100:
  x = int(input())
  if x == 1:
    continue
  if x > 12:
    continue
  if x != 0:
    if place + x <= 100:
      place += x
    if place == 9:
      place = 34
    elif place == 40:
      place = 64
    elif place == 67:
      place = 86
    if place == 54:
      place = 19
    elif place == 90:
      place = 48
    elif place == 99:
      place = 77
    if x != 0:
      print("You are now on square "+str(place))
  if x == 0:
    print("You Quit!")
    break
  if place == 100:
    print("You Win!")
    break
