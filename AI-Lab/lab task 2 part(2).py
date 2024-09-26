movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
sum = 0
for budget in movies:
  sum = sum+ budget[1]
avg=sum/len(movies)
high_budget_movie=0
for budget in movies:
  if budget[1] > avg:
    print(f'{budget[0]}, {budget[1]}, higher than average: {avg}')
    high_budget_movie +=1
print(f'high budget movies : {high_budget_movie}')