# Make the 'for' loop for 9 rows using a range of 0 - 10.
for i in range(0, 10):

# Create the iteration 'asterisk multiplied by i+space' to add spaces consecutively and apply the 'if' statement to limit the repeat up to line 5.
   if i < 6:
      print("*"*i+" ")

# Stop the iteration at line 5 and use back-slash n (\n) to print the remaining 4 lines of the pattern. End the loop with 'break'.
   elif i >= 6:
      print("****\n***\n**\n*")
      break


