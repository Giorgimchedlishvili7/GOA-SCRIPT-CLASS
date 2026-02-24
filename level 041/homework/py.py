#function named is_even
def is_even(list1):
    
    # Creates an empty list
    even = [] 

    # startss a for loop
    for i in list1:
        
        # dividing i
        if i % 2 == 0:
            
            # i need help with this
            even.append(i)
            
    # Once the loop finishes checking every number
    return even

# Calls the function
print(is_even([1,2,3,4,5,6,7,8,9,10]))