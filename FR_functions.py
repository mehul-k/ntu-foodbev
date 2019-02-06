import pygame
from time import sleep

def draw_circle(screen, user_location,destination=(0,0,0)):
   screenIm = pygame.image.load("ntu_map.png")
   screenIm = pygame.transform.scale(screenIm, (1400 , 750))
   
   screen.blit(screenIm,(0, 0)) 
   pygame.draw.circle(screen, (0,255,255), user_location, 10)
   if destination != (0,0,0):
      pygame.draw.circle(screen, (0,255,0), destination, 10)
   pygame.display.flip()
   
   
def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def get_right_input(price):
    if isfloat(price) == True:
                return float(price)
    else:
        while True:
            price = input("Invalid input! Try again:")
            if isfloat(price) == True:
                 return float(price)
                 break

def merge(left_list, right_list):
    # modified merge function which can compare relevant inner elements of the elements being compared
    result_list = []

    # while left and right list has elements
    while left_list and right_list:
        if left_list[0][2] < right_list[0][2]: # second index to compare the distances between the canteen when used by merge sort
            result_list.append(left_list[0])
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)

    #left list still contain elements. Append its contents to end of the result list
    if left_list:
        result_list.extend(left_list)
    else:
    #right list still contain elements. Append its contents to end of the result list
        result_list.extend(right_list)
    
    return result_list

def mergesort(list_of_items):
   # sorts the list using merge sort algorithm
    list_len = len(list_of_items)

    # base case
    if list_len < 2:
        return list_of_items
    left_list = list_of_items[:list_len // 2]   # //
    right_list = list_of_items[list_len // 2:]  # "//" to force division

    # merge sort left and right list recursively
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    return merge(left_list, right_list)

def distance_a_b(location_of_a,location_of_b):
    # This function takes the x,y coordinates of a and b and calculates
    # the straight line distance between them using Pythagoras' Theorem.
    # distance between a and b = pow(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)),0.5)
    x1=location_of_a[0] # x - coordinate of a
    x2=location_of_b[0] # x - coordinate of b
    y1=location_of_a[1] # x - coordinate of a
    y2=location_of_b[1] # y - coordinate of b
    distance = pow(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)),0.5)
    return distance

def sort_distance(user_location,canteens_location):
    # This function sorts the distance between the user location and canteens
    # location using the mergesort algorithm. Canteens_location will contain
    # a list of lists. Each list will contain the canteen's name in the first
    # entry and a tuple containing the canteen's location in the second one.

    # This for loop calculates the distance between each canteen and the user
    # and stores it as the last entry of the inner list for each respective
    # canteen.
    for i in range(len(canteens_location)):
        dist_user_canteen=distance_a_b(user_location,canteens_location[i][1])
        canteens_location[i].append(dist_user_canteen)
    # The distances are then sorted in ascending order. Hence, the nearest
    # canteen will have index 0.
    sorted_canteen=mergesort(canteens_location)
    # display the canteens and their distances
    print("These are the canteens and their distances away from you in ascending order:")
    print()
    for element in sorted_canteen:
       print('{:30}'.format(element[0]),round(element[-1]))
    print()
    # return nearest canteen, location and the distance
    return sorted_canteen

def search_by_food(foodname, foodlist_canteens):
    # This function searches all canteens to return the canteen with wanted food.
    # foodname is the food to be used as the search criteria
    # checks if the food is sold in the canteens by checking if its in the inner list of food sold at canteen
    # foodlist_canteens contains a lists of list where each inner list = [canteen name, types of food, rank of canteen]
    canteen_with_food = [] # empty list to store the  inner list of canteens with wanted food
    for i in range(len(foodlist_canteens)):
        if foodname in foodlist_canteens[i][1]:
            canteen_with_food.append(foodlist_canteens[i]) # if the canteen contains the food, append list to the empty list

    return canteen_with_food # returns lists of list of canteens with wanted food
            

def search_by_price(price, pricelist_canteens):
    # This function searches all canteens to return the food within the searched range.
    # price is a tuple with the range required by the user
    # pricelist_canteens contains a list of lists that contains the canteen name, prices of the food stalls and the corresponding type of food
    canteen_with_price = {} # creation of empty dictionary
    for i in range(len(pricelist_canteens)): # iterate through each canteen
       canteen_with_price[pricelist_canteens[i][0]]=[] # creates an empty list for canteen, i, in the dictionary with the key as the canteen name. 
       for j in range(len(pricelist_canteens[1])):
           if price[0]<= pricelist_canteens[i][1][j] and price[1]>= pricelist_canteens[i][1][j]: # if the price of the food in the canteen falls within range
               canteen_with_price[pricelist_canteens[i][0]].append(pricelist_canteens[i][2][j]) # appends the food that falls within range in the list created in outer loop

    # this for loop is used to remove canteens without any food within the price range from the dictionary
    for key in list(canteen_with_price):
       if canteen_with_price[key]==[]:
          del canteen_with_price[key]
          
    return canteen_with_price # returns dictionary with the canteen names as its keys and list containing the types of food within price range

def sort_by_rank(ranklist_canteens):
    def last(sequence):
        # function returns second element of sequence
        return sequence[-1] 
    ranklist_canteens.sort(key=last) # sort the ranklist_canteens based on the last element (ranking)

    # displays the rankings of the canteens in ascending order
    print("The rankings of canteens based on your search criteria in ascending order is:")
    print()
    for element in ranklist_canteens:
       print('{:30}'.format(element[0]))
    print()
    # returns list of canteen names in ascending order
    return ranklist_canteens

def MouseClick():
   finish = False
   while finish == False:
   ## pygame.event.get() retrieves all events made by user
      for event in pygame.event.get(): # if user clicks close 
        if event.type == pygame.QUIT:
           pygame.quit() # closes window
           finish = True
           return (None,None)
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            finish = True

   return (mouseX, mouseY)


def get_user_location():
   screen = pygame.display.set_mode((1400,750))
   mapImage = pygame.image.load("ntu_map.png")   # load ntu map
   mapImage = pygame.transform.scale(mapImage, (1400 , 750))
   # add the mapImage over the screen object
   screen.blit(mapImage,(0, 0))
   # load an image to tell user to click to indicate location, call this clickImage
   clickImage=pygame.image.load("click_location.png") 
   # add the clickImage over screen object
   screen.blit(clickImage,(0, 0))
   #will update the contents of the entire display window
   pygame.display.flip()   
   # get outputs of Mouseclick event handler 
   buttonX, buttonY = MouseClick()
   return (buttonX , buttonY)



def dest_displayer(canteen_name,user_location,dest):
   # this function draws the location of the user and a destination on the map
   print("Printing your location(CYAN) and destination(GREEN) on the map, please wait...")
   sleep(2) # provides buffer time for user to read the above message
   screen = pygame.display.set_mode((1400,750)) # sets size of window
   quitImage = pygame.image.load("quit.png") # loads a image for user to have a region to close the map
   draw_circle(screen,user_location,dest) # draws the 2 location on the map
   font = pygame.font.SysFont("monospace", 20) 
   text1 = font.render(str(canteen_name), True, (0, 255, 0)) # creates surface to render destination
   screen.blit(quitImage,(0, 0)) # blits quit image onto the screen
   screen.blit(text1,dest) #blits text onto the screen
   pygame.display.flip() # updates the screen 
   user_click= (500,500) # creates a variable with a default value as indicated so that the user can only close image if he click on the region covered by quit.png
   # allows the user to keep the screen as long as he does not click on image
   while (user_click[0]>149) or (user_click[1]>243):
      user_click=MouseClick()
   pygame.display.quit() # closes window

