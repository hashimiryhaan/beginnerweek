temp=0
list=[2,9,0,54,23]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
     if(list[i]>list[j]):
      temp=list[i]
      list[i]=list[j]
      list[j]=temp
#code for displaying the sorted list
print("sorted list",list)

