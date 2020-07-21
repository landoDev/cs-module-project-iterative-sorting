# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # for each element after this one:
        for unsorted in range(cur_index, len(arr)):
            # if that element is less than the smallest
            if arr[unsorted] < arr[smallest_index]:
                # set smallest to that element
                smallest_index = unsorted
        # TO-DO: swap
        # Your code here
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
        # put smallest in the first unsorted position


    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # set the master length
    end_list = len(arr)
    # Loop through the list 
    for item in range(end_list - 1):
        # for each item, check the value of the next index 
        for compared in range(0, end_list - item - 1):
            # if the value on the right is higher, switch them  
            if arr[compared] > arr[compared +1]:
                arr[compared], arr[compared +1] = arr[compared + 1], arr[compared]

    # Question: I track how this works but I can't nail down how this actually ever leaves this loop. Is it because the nested for loop happens at each element so it runs through the list starting from index 0? what if there was a lower number in the back? Update, the - item in the for loop resets where the end of the list has something to do with it.

    # first attempt had the right idea, but didn't use the master for loop
    # loop over array
    # while True:
    #     end_list = len(arr)
    #     # initialize original index
    #     for item in range(0, end_list -1):
    #         next_item = arr[item +1]
    #         if item > next_item:
    #             arr[next_item], arr[item] = arr[item], arr[next_item]
    #             end_list -= 1




    return arr

print(bubble_sort([12,45,35,2,5,7,8]))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
