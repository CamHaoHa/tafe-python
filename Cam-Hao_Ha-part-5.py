print("please enter your 5 marks below")
# read 5 input and change the data value to float
marksList = []
def getMarks():
    while True:
        try:
            mark1 = float(input("enter mark 1: "))
            validMarks(mark1)
            mark2 = float(input("enter mark 2: "))
            validMarks(mark2)
            mark3 = float(input("enter mark 3: "))
            validMarks(mark3)
            mark4 = float(input("enter mark 4: "))
            validMarks(mark4)
            mark5 = float(input("enter mark 5: "))
            validMarks(mark5)
        except ValueError:  #print message to user 
            print(" Please enter a number from 0-100!!!")
        else:
            sumOfMarks = sum(marksList)
            averageOfMarks = sum(marksList)/5
            print("The sum of your marks is: "+str(sumOfMarks))
            print("The average of your marks is: "+str(averageOfMarks))
            break

# condition check, input need to be between 0 to 100
def validMarks(mark):
    if (mark > 0 and mark <100):
        marksList.append(mark)
    else:
        raise ValueError


getMarks()


