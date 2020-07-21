5
[3, 38, 44, 5]
[3, 38, 44, 44]
[3, 38]
def insertion_sort(input_list):
    # separate the first element 
    # think of it as sorted
    # no code required (abstract step) // the first element itself is "sorted"

    # for all unsorted items
    for i in range(1, len(input_list)): # we want to start AFTER the first element since it's "separated"
        # mark the current item we are considering
        current = input_list[i]
        j = i
        # look left until we find the proper place to insert the current item
        # as we are "looking left", we need to shift items to the right
        while j > 0 and current < input_list[j - 1]: # we aren't at the beginning and
            # current is less than "left"
            # shift the item to the right
            input_list[j] = input_list[j - 1]
            j -= 1
            # the while loop shifts everything right one and finds the insertion point
            # now that we've found the insertion point

            # insert item
            input_list[j] = current
    return input_list

print(insertion_sort([4,3,67,74,1,23,90]))