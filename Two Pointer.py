def reverse_list(lst):
    #initialize the first pointer at first index
    pointer_left = 0

    #initialize second pointer at second index
    pointer_right = len(lst)-1

    #swap list index while left point is less than right
    while pointer_left < pointer_right:

        lst[pointer_left],lst[pointer_right] = lst[pointer_right],lst[pointer_left]
    
        pointer_left  += 1
        pointer_right -=1
        
    return lst
        
list1 = [1, 2, 3, 4, 5]
print(reverse_list(list1))
