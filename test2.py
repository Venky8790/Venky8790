# defining the bubble sort function
def bubble_sort(data):
    input_list = list(data)
    for i in range(len(input_list)-1):
        for j in range(len(input_list)-1 -i):
            #comparing the adjucent values
            if input_list[j] > input_list[j+1]:
               # print(type(input_list))
                # Swaping the input_list[j+1] and input_list[j]
                temp = input_list[j]
                input_list[j] = input_list[j+1]
                input_list[j+1]= temp
    
    print("The output of bubble sort is : ",input_list)


data = [10,2,9,17,-1,97] # list
data1 = (-1,20,15,7,98,6) # tuple

# calling the bubble sort function for list
bubble_sort(data)

# calling the bubble sort function for tuple
bubble_sort(data1)
bubble_sort("string")