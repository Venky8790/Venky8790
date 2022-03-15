# defining the bubble sort function
def bubble_sort(input_list):

    #input_list = list(data)

    for i in range(len(input_list)-1):

        for j in range(len(input_list)-1 -i):

            #comparing the adjucent values
            if input_list[j] > input_list[j+1]:
                
                # Swaping the input_list[j+1] and input_list[j]
                input_list[j],input_list[j+1] = input_list[j+1],input_list[j]
                
    print("The output of bubble sort is : ",input_list)


data = [10,2,9,17,-1,97] # list
data1 = (-1,20,15,7,98,6) # tuple
data2 = "string" # string

# calling the bubble sort function for list
bubble_sort(list(data))

# calling the bubble sort function for tuple
bubble_sort(list(data1))

# calling the bubble sort function for string
bubble_sort(list(data2))