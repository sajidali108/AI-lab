def FizzBuzz(limit):
  for i in range(1,limit):
    if i % 3==0 and i % 5==0:
      print('FizzBuzz')
    elif i % 3==0:
      print('Fizz')
    elif i % 5==0:
      print("Buzz")
    else:
      print(limit)

FizzBuzz(9)