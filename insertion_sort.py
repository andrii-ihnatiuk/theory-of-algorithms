# insertion sort
array = [28, 76, 27, 10, 5, 35, 95, 16, 33] # defining an array
temp = 0 # for the element we stay on = 0 # to move along the array
iter = 0
# main cycle
for i in range(1, len(array)):
  j = i-1 # defining a start position to compare with
  temp = array[i] # the element we want to place in the right position
  # this cycle finds the home for the element
  while j >= 0 and array[j] > temp:
    array[j+1] = array[j]
    j-=1
  array[j+1] = temp # putting remembered element to the position 
                    # that was found in 'while' cycle

  
for i in array: 
  print(i)
