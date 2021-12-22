def solution(A):
   sum_of_numbers = 0
   length = len(A)
   index = 0
   counter = 0
   while index < length:
       value = A[index]
       if sum_of_numbers + value > 0:
           sum_of_numbers = sum_of_numbers + value
           index = index + 1
       elif sum_of_numbers + value == 0:
           if index != (length - 1):
               if A[index + 1] > 0:
                   sum_of_numbers = sum_of_numbers + value
                   index = index + 1
               else:
                   A.append(value)
                   length = length + 1
                   counter = counter + 1
                   index = index + 1
           else:
               index = index + 1
 
       else:
           A.append(value)
           length = length + 1
           counter = counter + 1
           index = index + 1
 
   return counter