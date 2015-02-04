inputstring = input("please enter the string")
startindexin = input("please enter the starting index 1")
finishindexin = input("please enter the finish index 1")
startindexin2 = input("please enter the starting index 2")
finishindexin2 = input("please enter the finish index 2")


startindex=int(startindexin)
finishindex =int(finishindexin)+1
startindex2=int(startindexin2)
finishindex2 =int(finishindexin2)+1

print(inputstring[startindex:finishindex],inputstring[startindex2:finishindex2])
