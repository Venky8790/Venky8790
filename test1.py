data = [1,2,4,5,9,-1,9]
for i in range(len(data)-1):
     for j in range(len(data)-1 -i) :
        if data[j] > data[j+1]:
           data[j],data[j+1] = data[j+1],data[j]

print("The output of bubble sort is : ",data)