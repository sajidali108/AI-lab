account_num= 4782780001616401
acc=str(account_num)

upd_account_num=acc[:-1]
#upd_account_num=(upd_account_num)
print(upd_account_num)
rev_acc_num=upd_account_num[::-1]
print(rev_acc_num)

list1=[]
index=0
for digit in rev_acc_num:
  integ= int(digit)
  if index % 2 == 0:
    integ*=2
  list1.append(integ)

  index=index +1
print(list1)

list2=[]
for value in list1:
  if value>9:
    sub=value-9
  else:
    sub=value
  list2.append(sub)
print(list2)

sum= 0
for num in list2:
  sum = sum + num

remov_digit=int(acc[-1])
sum=sum+remov_digit
print(sum)

if sum/10:
  print('yes it is account number (valid)')

#st=str(account_num)

#x_acc_num=account_num[:-1]+'x'
#x_acc_num=int(x_acc_num)
#print(x_acc_num)

#reverse_num=x_acc_num[:-1].reverse()


#for i in x_acc_num.index(i+2)