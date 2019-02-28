#For writing the number of days until christmas we need to have the 'date' and 'datetime' functions from the datetime library.
from datetime import datetime, date
 
#Draws a christmas tree!
 
#Width of tree in letters, we will use this later.
width = 50
 
#The text that makes up the space around the tree-
# (to use later). The text is what is inside the quotes,
# a single space.
spaceText = " "
 
#The text that makes up the leaves
leavesText = "v"
 
#Alternate leaves text, to give the tree some texture.
leavesText2 = "V"
 
#Text for the trunk
trunkText = "#"
 
#Do this for each number from zero to width.
for number in range(0, width):
 
    #How many leaves should the tree have at this branch?
        # 'leaves' now contains the current value of 'number'.
        leaves = number
 
        #How much space does that leave?
        # The space on each side of the tree is just the space
        # not taken up by the leaves.
        # 'space' is now contains the width of our tree minus the
        # current number of leaves on this branch.
        space = width - leaves
 
        #The space is not all on one side of the tree, though, it's eaven on both sides!
        # space now contains half the value it did before.
        # the 'int' function chops off the decimal part- we can't have a half or a quarter of a letter!
        space = int(space / 2)
 
        #We should decide what our leaf should look like. Here, every even numbered -every other- branch is v instead of V,
        # and the first ever leaf is a star.
        if number == 1:
                #Store what the leaf should look like in thisLeaf.
                thisLeaf = "*"
        #If the number was not one, the program reads this; elif stands for "else, if".
        # check to see if the number is even. '%' is like '/', divide, but instead it gives us the remainder,
        # if it divide by 2 with no remainder, it must be an even number
        elif number % 2 == 0:
                #We store our choice in thisLeaf
                thisLeaf = leavesText
        #If it did not divide evenly by two (if it was an odd number), the computer does the procedure in 'else'.
        else:
                thisLeaf = leavesText2
 
        #Here we make the text that looks like this branch of the tree
        # we 'add' the text together, as well as 'multiplying' to get a certian number
        # of our text; "A" * 3 would become AAA.
        branch = (space * spaceText) + (leaves * thisLeaf)
 
        #'Type' out this branch of the tree, using the function print,
        # which tells the program to display the text it is sent.
        print(branch)
 
#Write the trunk of the tree
# the trunk of the tree should be about one sixth of its width.
# again, we chop off the decimal.
trunkWidth = int(width / 6)
 
trunk = trunkText * trunkWidth
 
#How much space?
# we need the trunk in the center, so the space should be half the width of the tree
# minus half the width of the trunk.
spaceText = " " * int( (width/2) - (trunkWidth/2) )
 
#How tall should the trunk be?
# about one-tenth of the tree's height.
trunkHeight = int(width / 10)
 
#From zero to trunkHeight-
for number in range(0, trunkHeight):
        #Type out the trunk!
        print(spaceText + trunk)
 
#Calculate in the number of days until christmas-
# it's the date of christmas minus the date of now.
untilChristmas = date(2012, 12, 25) - datetime.now().date()
 
#The str function converts our number of days to text, so we can
# add it to the rest of the text.
christmasText = "There are " + str(untilChristmas.days) + " days until christmas!"
 
#Here I make textSpace (empty) just in case we want to try to center the text using space
textSpace = ""
 
#We would like this text to be centered if we have an especially big tree
# I use the len() function, which tells me the length of my text in letters.
if width > len(christmasText):
 
        #To center the text, we push it to the side by half the width of the tree
        # minus half the width of the text as we did with the trunk.
        textSpace = " " * int( (width/2) - (len(christmasText)/2) )
 
#Type out the message
print(textSpace + christmasText)
