#Method 1
#A very "direct" way of printing the result.
#But it does not meet the criteria of:
#Being able to work with newly added list value
#Also this code is really long, imagine if it contained 250 items in list.

spam = ['apples' , 'bananas', 'tofu', 'cats']
print(spam[0], spam[1], spam[2], 'and ' + (spam[3]), sep=', ')

#Method 2
#This method is not taught if your only up to Chapter 4 in ATBS.
#While working this exercise, I had trouble printing the items without the brackets.
#Refer https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python
#I learnt the function of *value, which unpacks the list
#Also as you can see, compared to method 1
#I used -1 when slicing.
#*spam[:-1] gives me all items in list except the last item
#spam[-1] gives me the last item.
#so if I were to add new item, the function will still work.

spam = ['apples', 'bananas', 'tofu', 'cats']
print(*spam[:-1], 'and ' + spam[-1], sep=', ')

#Method 3
#This method does not include things exceeding Chapter 4 in ATBS.
#Refer https://stackoverflow.com/questions/51905174/comma-code-program-from-automate-the-boring-stuff-with-python
#Using for loop, we can go through items in spam except [-1], which is the last item.
#By using  end=',' we stops the print function from going to the next line.
#So for each iteration of the for loop, it will print in 1 line.
spam = ['apples', 'bananas', 'tofu', 'cats']
for i in spam[:-1]:
    print(i, end=', ')
print('and ' + spam[-1])
