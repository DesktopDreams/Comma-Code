#Comma Code Project.

itemList = [ ] #Assign an empty list to a variable
print('To use this program, enter itemGather() to add data. ' + \
      'Use itemRemove() to remove data. ' + \
      'Use readBetter() to view data clearly.')
      
def itemGather():
    global itemList #To change value in the itemList outside this function.
    while True:
        print('Type in your favourite countries')
        a = input()
        if a == '': #The code stops looping if user inputs nothing.
            break
        else:
            itemList.append(a) #Adds new items to list per loop.
            continue

def itemRemove():
    global itemList
    while True:
        try:
            print('Which country do you want to remove')
            b = input()
        except ValueError and TypeError:
            continue
        if b == '':
            break
        else:
            itemList.remove(b)
            continue

def readBetter():
    for i in itemList[:-1]:  #Exclude the last item in the list
        print(i, end=', ') #The end=', ' allows the printed text to stay in 1 line
    print('and ', itemList[-1], end='.')
    return
           


