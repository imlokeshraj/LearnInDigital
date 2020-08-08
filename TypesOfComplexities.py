### Types of Complexities ###

cuisines = ['Indian','Chinese','Italian','French']
dishes = {cuisines[0]:['Biryani','Naan','Roti'],
		  cuisines[1]:['Dim Sums','Noodles','Spring Rolls','Fried Rice'],
		  cuisines[2]:['Panzenella','Bruschetta','Margherita Pizza'],
		  cuisines[3]:['Cassoulet','Flamiche','Ratatouille']}

### Constant | O(1) ###
print("\n### Constant Function ###")
print("I have decided to go with Fried Rice before entering the restaurant.\nso I am not interested to know the menu")

print("Ordered : " + dishes['Chinese'][3])

### Logarithmic | O(logn) ###
print("\n### Logarithmic Function ###")
print("I have decided to go with either Chinese or Italian before entering the restaurant.\nso I am not interested to know the Indian and French menu")

myChoiceCuisine = ['Chinese','Italian']
for myCuisine in myChoiceCuisine:
	print(dishes[myCuisine])
print("I will go with Italian cuisine. And I am okay with Margherita Pizza")
print("Ordered : " + dishes['Italian'][2])

### Linear | O(n) ###
print("\n### Linear Function ###")
print("Say me the entire menu available irrespective of Cuisine")

for dish in dishes:
	print(dishes[dish])

### Linearithmic  | O(nlogn) ###
print("\n### Linearithmic Function ###")
print("Say me the Cuisines available")

for cuisine in cuisines:
	print(cuisine + ". Are you Interested sir? <yes/no>")
	choice = input()
	if (choice == "yes"):
		print("The dishes in " + cuisine + " are")
		for cuisineDish in dishes[cuisine]:
			print(cuisineDish)

### Quadratic | O(nlogn) ###
print("\n### Quadratic Function ###")
print("Say me all the Cuisines and the respective dishes to the specific cuisine available")

for cuisine in cuisines:
	print(cuisine)
	print("The dishes in " + cuisine + " are")
	for cuisineDish in dishes[cuisine]:
		print(cuisineDish)


### Lokesh Raj M | Learn in Digital ###
