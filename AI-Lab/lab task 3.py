class MultiReflexAgent:
  def __init__(self,temp):
    self.desired_temp=temp

  def percept(self,temp):
    self.current_temp=temp

  def act(self):
    if self.current_temp > self.desired_temp:
      return "Turn off the heater"
    else:
      return "Turn on the heater"
agent=MultiReflexAgent(22)
agent.percept(16)
agent.act()
rooms= {
    'living room' : 28,
    'bedroom' : 18,
    'kitchen' : 32
}
for room, temp in rooms.items():
  agent.percept(temp)
  print(f'{room}:{temp}==>{agent.act()}')