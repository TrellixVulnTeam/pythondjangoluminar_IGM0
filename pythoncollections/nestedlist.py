students=[
    [10,"ajay","bca",250],
    [11,"vjay","bca",240],
    [12,"sibin","bca",220],
    [13,"dino","mca",220],
    [14,"tom","mca",180],
    [15,"jain","mca",250],
]

#for stud in students:
 #   if(stud[3]>240):
  #      print(stud[1])


#print total sumof total
#marks=0
#for stud in students:
    #marks=marks+stud[3]
#print("total =",marks)




##calculate total of bca and mca seperately

mtotal,btotal=0,0
for stud in students:
    if stud[2]=="bca":
        btotal+=stud[3]
    else:
        mtotal+=stud[3]
print("bca total",btotal)
print("mca total",mtotal)



