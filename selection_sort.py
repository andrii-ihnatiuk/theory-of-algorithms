# selection sort

array = [28, 76, 27, 10, 5, 35, 95, 16, 33] # defining an array
temp = 0; # to exchange the elements
min_index = 0 # needed to remember index of the 
              # smallest element of array's part
i = 0; j = 0  # to move along the array

# main cycle
for i in range(len(array)):
  min_index = i # assigning a start value
  # this cycle finds out the minimum value in the rest of the array
  for j in range(i+1, len(array)):
    # comparing elements to find the min index
    if array[j] < array[min_index]: min_index = j
  # placing found element to the right position
  temp = array[min_index]
  array[min_index] = array[i] 
  array[i] = temp

for i in array: 
  print(i)
