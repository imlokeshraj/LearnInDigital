### Estimating The Time Complexity ###

blogName = 'Learn in Digital'	# Count = 1 time
n = 5;							# Count = 1 time
for i in range(n):				# Count = n + 1 times (i.e.) in this case it is 6 (5 + 1) times
	print(blogName)				# Count = n times (i.e.) in this case it is 5 times

# Sum of Counts = 1 + 1 + (n + 1) + n
#               = 2n + 3

# Estimation
# Neglect Leading Constants = n + 3
# Neglect Lower Order terms = n

### So the Time Complexity here is O(n) ###

### Lokesh Raj M | Learn in Digital ###