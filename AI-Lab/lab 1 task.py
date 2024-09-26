
#class DynamicCal:
def inputexpression(expression):
    stack_num=[]
    stack_op=[]
    i=0
    while i<len(expression):
      exp_num=expression[i]
      if exp_num.isdigit():
        num=0
        while i<len(expression) and expression[i].isdigit():
          num=num*10+int(expression[i])
          i=i+1
        stack_num.append(num)
        continue
      if exp_num in "+-*/":
        stack_op.append(exp_num)
      i=i+1
    #performing operations:
    x=0
    while x<len(stack_op):
      if stack_op[x] in '/*':
        if stack_op[x]=='/':
          sol=stack_num[x] / stack_num[x+1]
        elif stack_op[x]=='*':
          sol=stack_num[x] * stack_num[x+1]

        # updating the stack for results
        stack_num[x]=sol
        stack_num.pop(x+1)
        stack_op.pop(x)

      else:
        x=x+1
    x=0
    while x<len(stack_op):
      if stack_op[x]=='+':
        sol= stack_num[x]+stack_num[x+1]
      elif stack_op[x]=='-':
        sol=stack_num[x] - stack_num[x+1]

      stack_num[x]=sol
      stack_num.pop(x+1)
      stack_op.pop(x)

    return stack_num[0]


#dyc=DynamicCal()
#dyc.inputexpression()
sol=inputexpression('8/4*2+9-1')
print(sol)

