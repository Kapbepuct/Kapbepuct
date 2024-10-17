immutable_var = 'string',1234,False,[0,'hug']
print(immutable_var)
# immutable_var[0] = 1 . кортеж нельзя изменить, в отличии от списка
mutable_list = [1,2,3,'fake',[1,2]]
print(mutable_list)
mutable_list[2] = 'tree'
mutable_list[4][0] = 222
summ = mutable_list[0] + mutable_list[1]
print(summ)
print(mutable_list)