enter_number = int(input('Enter a four-digit number:'))
digits1 = enter_number // 1000
digits4 = enter_number % 10
digits2 = (enter_number//100) % 10
digits3 = (enter_number//10) % 10 
print (f'Multiplication of digits in {enter_number} is ', digits1*digits2*digits3*digits4)
print (f'Reversing of digits  in {enter_number} is ', digits4*1000+digits3*100+digits2*10+digits1)
number_list = list (str(enter_number))
print (f'Sorting of digits  in {enter_number} is ',''.join(sorted (number_list)))
