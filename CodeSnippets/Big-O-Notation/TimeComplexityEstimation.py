### Estimating The Time Complexity ###

blogName = 'Learn in Digital'	# Count = 1 time
n = 5;							# Count = 1 time
for i in range(n):				# Count = n times (i.e.) in this case it is 5 times
	print(blogName)				# Count = n times (i.e.) in this case it is 5 times

# Sum of Counts = 1 + 1 + n + n
#               = 2n + 2

# Estimation
# Neglect Leading Constants = n + 2
# Neglect Lower Order terms = n
# So the Time Complexity here is O(n)

### Lokesh Raj M | Learn in Digital ###
