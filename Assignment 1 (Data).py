import time

print("---- Task 1: Chocolate Distribution Algorithm ---- ") #O(1)
def distribute_chocolates_iterative(chocolates, students): #O(1) #creating a function for iteration with the parameters chocolate and students
    print("\nIterative function ") #O(1)
    distributed_chocolates = []  #O(1) # To keep track of chocolates distributed to students
    steps = 0 #O(1) #to count the number of steps it took
    sec_iterative = time.time()
    print("The time it took for the iterative function in seconds is:", sec_iterative)
    # Iterate over each student
    for student in students: #O(n)
        if chocolates: #O(1)
            distributed_chocolates.append((student, chocolates.pop(0))) #O(n) #add the chocolates and poping it from the list
            steps += 1 #to add steps to the count #O(1)
        else: #O(1)
            print("Not enough chocolates for all students!") #O(1)
            break  #O(1) # Exit the loop
    print("Number of steps executed are : ", steps) #O(1)
    return distributed_chocolates #O(1)



# ----------------------------------------------------------------------
def distribute_chocolates_recursive(chocolates, students, distributed_chocolates=None, steps=0): #O(1) #function for recursive with its parameters
    if distributed_chocolates is None: #O(1)
        print("\nRecursive function ") #O(1)
        distributed_chocolates = [] #O(1) #the list where it will add the outcomes
    sec_recursive = time.time()
    print("The time it took for the recursive function in seconds is:", sec_recursive)
    # Base case: No more students or chocolates left (this is when it will stop)
    if not students:
        print("\nNot enough students, so recursive function stops") #O(1)
        print("Number of steps executed are : ", steps) #O(1)
        return distributed_chocolates #O(1)

    if not chocolates:
        print("\nNot enough chocolates, so recursive function stops") #O(1)
        print("Number of steps executed are : ", steps) #O(1)
        return distributed_chocolates #O(1)

    # Assign the first chocolate to the first student and it adds it to 'distributed_chocolates'
    distributed_chocolates.append((students[0], chocolates[0])) #O(1)
    steps += 1 #O(1)
    # Recursive call: it calls itself with the remaining chocolates and students excluding the first one
    return distribute_chocolates_recursive(chocolates[1:], students[1:], distributed_chocolates, steps) #O(n)

# ----------------------------------------------------------------------
# Test case 1: Equal number of chocolates and students
print("\n-----TEST 1: Equal number of students and chocolates----------")
#the chocolates that we have
chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"},
    {"weight": 6, "price": 3, "type": "Dark Chocolate", "ID": "008"},
    {"weight": 10, "price": 8, "type": "Milk Chocolate", "ID": "004"},
    {"weight": 2, "price": 1, "type": "White Chocolate", "ID": "006"},
    {"weight": 4, "price": 6, "type": "Strawberry Chocolate", "ID": "010"},
    {"weight": 3, "price": 5, "type": "Salted Chocolate", "ID": "012"}
]
#the students we have
students = ["Alice", "Amy", "Tom", "John","Bob", "Emily", "Charlie"]
result_iter = distribute_chocolates_iterative(chocolates, students) #calling the iterative function

chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"},
    {"weight": 6, "price": 3, "type": "Dark Chocolate", "ID": "008"},
    {"weight": 10, "price": 8, "type": "Milk Chocolate", "ID": "004"},
    {"weight": 2, "price": 1, "type": "White Chocolate", "ID": "006"},
    {"weight": 4, "price": 6, "type": "Strawberry Chocolate", "ID": "010"},
    {"weight": 3, "price": 5, "type": "Salted Chocolate", "ID": "012"}
]

result_rec = distribute_chocolates_recursive(chocolates, students) #calling the recursive function

expected_result = [
    ('Alice', {'weight': 5, 'price': 2, 'type': 'Almond Chocolate', 'ID': '002'}),
    ('Amy', {'weight': 7, 'price': 4, 'type': 'Peanut Butter Chocolate', 'ID': '005'}),
    ('Tom', {'weight': 6, 'price': 3, 'type': 'Dark Chocolate', 'ID': '008'}),
    ('John', {'weight': 10, 'price': 8, 'type': 'Milk Chocolate', 'ID': '004'}),
    ('Bob', {'weight': 2, 'price': 1, 'type': 'White Chocolate', 'ID': '006'}),
    ('Emily', {'weight': 4, 'price': 6, 'type': 'Strawberry Chocolate', 'ID': '010'}),
    ('Charlie', {'weight': 3, 'price': 5, 'type': 'Salted Chocolate', 'ID': '012'})
]

print("\nExpected results is ", expected_result)
print("\nIterative result is ", result_iter)
print("\nRecursive result is ", result_rec)

# -----------------------------------------------------------------------------------------
# Test case 2: More students than chocolates
print("\n-----TEST 2: More students less chocolates----------")
chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"}
]
students = ["Alice", "Amy", "Tom"]
result_iter = distribute_chocolates_iterative(chocolates, students)

chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"}
]
result_rec = distribute_chocolates_recursive(chocolates, students)

expected_result = [("Alice", {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"})]

print("\nExpected results is ", expected_result)
print("\nIterative result is ", result_iter)
print("\nRecursive result is ", result_rec)

# -----------------------------------------------------------------------------------------
# Test case 3: More chocolates than students
print("\n-----TEST 3: More chocolates less students----------")
chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"}
]
students = ["Alice"]
result_iter = distribute_chocolates_iterative(chocolates, students)

chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"}
]

result_rec = distribute_chocolates_recursive(chocolates, students)

expected_result = [("Alice", {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"})]

print("\nExpected results is ", expected_result)
print("\nIterative result is ", result_iter)
print("\nRecursive result is ", result_rec)

# -----------------------------------------------------------------------------------------
print("\n---- Task 2: Sorting the Chocolates ---- ") #O(1)
def merge_sort_chocolates(chocolates, param): #O(1) #function for sorting  which the parameters chocolate and parm which can be either weight or price
    steps = [0]  #O(1) # number of  steps (it will keep track of the number of steps)

    # this is an inner function its responsibility is to merge left and right in a single sorted list based on the parameter
    def merge(left_half, right_half, chocolates, param): #O(1)
        i = j = k = 0 #O(1) #making them all equal to zero (the initialization phase of loops)

#while loops to iterate in the left and right and compare i and j
        while i < len(left_half) and j < len(right_half): #O(n)
            if left_half[i][param] < right_half[j][param]: #O(1) #checking the values
                chocolates[k] = left_half[i] #O(1) # copy an element from the left_half list to the chocolates list
                i += 1 #O(1) #increases the index i by 1
            else:
                chocolates[k] = right_half[j] #O(1) #copy an element from the right_half list to the chocolates list
                j += 1 #O(1) #increases the index j by 1
            k += 1 #O(1) #increases the index k by 1
            steps[0] += 1 #O(1)
        #these two while loops looks at the remaining left and right elements and copies them into 'chocolates'
        while i < len(left_half): #O(n)
            chocolates[k] = left_half[i] #O(1)
            i += 1 #O(1) #increases the index i by 1
            k += 1 #O(1) #increases the index k by 1
            steps[0] += 1  #O(1) # Increment steps

        while j < len(right_half): #O(n)
            chocolates[k] = right_half[j] #O(1)
            j += 1 #O(1)
            k += 1 #O(1)
            steps[0] += 1 #O(1)

    #base case for the merge sort algorithm (it will stop)
    if len(chocolates) <= 1: #O(1)
        return chocolates #O(1)

    #dividing the list into haves
    mid = len(chocolates) // 2 #O(1)
    left_half = chocolates[:mid] #O(1)
    right_half = chocolates[mid:] #O(1)

    #calls the function
    merge_sort_chocolates(left_half, param) #O(log n)
    merge_sort_chocolates(right_half, param) #O(log n)

    merge(left_half, right_half, chocolates, param) #it merges everything

    print("\nNumber of steps executed are : ", steps)
    sec_merge = time.time()
    print("The time it took for merge sort in seconds is:", sec_merge)
    return chocolates


chocolates = [
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"},
    {"weight": 6, "price": 3, "type": "Dark Chocolate", "ID": "008"},
    {"weight": 10, "price": 8, "type": "Milk Chocolate", "ID": "004"},
    {"weight": 2, "price": 1, "type": "White Chocolate", "ID": "006"},
    {"weight": 4, "price": 6, "type": "Strawberry Chocolate", "ID": "010"},
    {"weight": 3, "price": 5, "type": "Salted Chocolate", "ID": "012"}
]

# Test sorting by weight
sorted_by_weight = merge_sort_chocolates(chocolates.copy(), 'weight')

expected_by_weight = [
    {"weight": 2, "price": 1, "type": "White Chocolate", "ID": "006"},
    {"weight": 3, "price": 5, "type": "Salted Chocolate", "ID": "012"},
    {"weight": 4, "price": 6, "type": "Strawberry Chocolate", "ID": "010"},
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 6, "price": 3, "type": "Dark Chocolate", "ID": "008"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"},
    {"weight": 10, "price": 8, "type": "Milk Chocolate", "ID": "004"}

]
print("\n--Sort by weight--")
print("\nBefore sorting by weight", chocolates)
print("\nExpected Outcome: Sorted by weight ", expected_by_weight)
print("\nActual Outcome: Sorted by weight ", sorted_by_weight)

# Test sorting by price
sorted_by_price = merge_sort_chocolates(chocolates.copy(), 'price')
expected_by_price = [
    {"weight": 2, "price": 1, "type": "White Chocolate", "ID": "006"},
    {"weight": 5, "price": 2, "type": "Almond Chocolate", "ID": "002"},
    {"weight": 6, "price": 3, "type": "Dark Chocolate", "ID": "008"},
    {"weight": 7, "price": 4, "type": "Peanut Butter Chocolate", "ID": "005"},
    {"weight": 3, "price": 5, "type": "Salted Chocolate", "ID": "012"},
    {"weight": 4, "price": 6, "type": "Strawberry Chocolate", "ID": "010"},
    {"weight": 10, "price": 8, "type": "Milk Chocolate", "ID": "004"}

]
print("\n--Sort by price--")
print("\nBefore sorting by price", chocolates)
print("\nExpected Outcome: Sorted by price ", expected_by_price)
print("\nActual Outcome : Sorted by price ", sorted_by_price)

# -----------------------------------------------------------------------------------------
print("\n---- Task 3: Searching for a Specific Chocolate by weight and price---- ") #O(1)
def binary_search_chocolate(chocolates_assigned_to_students, criterion, value): #O(1)
    left = 0  #O(1) # starting index of array
    right = len(chocolates_assigned_to_students) - 1  #O(1) # end index of array
    steps = 0 #O(1)

    while left <= right: #O(log n)
        steps += 1 #O(1)
        mid = (left + right) // 2  #O(1) #finding middle value of index

        #checking if the value of the criterion is equal to the value
        if chocolates_assigned_to_students[mid][criterion] == value: #O(1)
            print("\nnumber of steps taken by the code is ", steps) #O(1)
            return chocolates_assigned_to_students[mid] #O(1)
        #making the search range less by searching the upper half
        elif chocolates_assigned_to_students[mid][criterion] < value: #O(1)
            left = mid + 1 #O(1)
        #searching the lower half
        else:
            right = mid - 1 #O(1)

    print("\nnumber of steps taken by the code is ", steps) #O(1)
    print(f" The {criterion} value : ", value, " is not found !") #O(1)
    return None #O(1)


chocolates_assigned_to_students = [
    {'Student': 'Alice', 'weight': 5, 'price': 2, 'type': 'Almond Chocolate', 'ID': '002'},
    {'Student': 'Amy', 'weight': 7, 'price': 4, 'type': 'Peanut Butter Chocolate', 'ID': '005'},
    {'Student': 'Tom', 'weight': 6, 'price': 3, 'type': 'Dark Chocolate', 'ID': '008'},
    {'Student':'John', 'weight': 10, 'price': 8, 'type': 'Milk Chocolate', 'ID': '004'},
    {'Student': 'Bob', 'weight': 2, 'price': 1, 'type': 'White Chocolate', 'ID': '006'},
    {'Student': 'Emily', 'weight': 4, 'price': 6, 'type': 'Strawberry Chocolate', 'ID': '010'},
    {'Student': 'Charlie', 'weight': 3, 'price': 5, 'type': 'Salted Chocolate', 'ID': '012'}
]

# Test searching by weight
# Step 1 : sort the data which is already done above
sorted_chocolates_by_weight = merge_sort_chocolates(chocolates_assigned_to_students, 'weight')
# Step 2 : search the element
result_weight = binary_search_chocolate(sorted_chocolates_by_weight, 'weight', 7) #changing the searched value here

print("-Searching by weight result is:-",result_weight)  # return None if weight value not found

# Test searching by price
sorted_chocolates_by_price = merge_sort_chocolates(chocolates_assigned_to_students, 'price')
result_price = binary_search_chocolate(sorted_chocolates_by_price, 'price', 6) #changing the searched value here

print("-Searching by price result is:-",result_price)  # return None if price value not found



