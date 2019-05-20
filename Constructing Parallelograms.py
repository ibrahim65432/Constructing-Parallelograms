#Constructing a rectange using height, width, and character. 
def Make_character_rectangle(height, width, char):
    row = 1
    while(row <= height):
        print(width*char)
        row+=1
Make_character_rectangle(2, 3, "^")

#The parallelogram has to be slanted, so we need to consider the spaces that will be present in the beginning
def Make_character_parallelogram(height,width,char):
    row= 1
    while(row <= height):
        #height-row is multiplied by space because the number of space in the beginning is equal to height-row.
       print((height-row)*' '+ (width*char))
       row+=1
Make_character_parallelogram(8,19,'&')
