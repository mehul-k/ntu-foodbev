import pygame
from FR_functions import *
from Locations import *
from time import sleep

# define a main function
def main():
    # initialise the pygame module
    pygame.init()
    print()
    # define a variable to control the main loop
    running = True
    # main loop
    while running:       
        repeater='not chosen' # repeater is a variable to determine if the program should keep running, 'not chosen' means that the user hasn't chosen any choice
        dest_display='' # variable used to indicate if the user wants to display dest on map
        pygame.display.set_caption("F&B Recommender System") # name of window
        screen = pygame.display.set_mode((1400,750)) # set size of window
        pygame.event.clear() # clear any previous events
        screenIm = pygame.image.load("header.png") # load header
        screenIm = pygame.transform.scale(screenIm, (1400 , 750)) # scales header
        screen.blit(screenIm,(0, 0)) # blits header
        pygame.display.flip() # update the screen with header
        choice = MouseClick() # finds the location which user clicks which indicates their choice on main screen
        
        if choice == (None,None): # user clicks on the close button of the window
            break # if user clicks on the close button of the window, allows the program to end without any errors
        
        if (50<=choice[0]<=377) and 400<=choice[1]<=540: # User clicks on distance
            repeater='chosen' # changes the repeater variable to indicate the user has chosen a choice
            
            user_location=get_user_location() # gets the user location
            if user_location == (None,None): # user clicks on the close button of the window
                break # if user clicks on the close button of the window, allows the program to end without any errors
            draw_circle(screen,user_location) # draws a circle of the user location in cyan
            pygame.display.quit() # closes window to bring user to python terminal
            
            canteen_loc=[] # a variable that will contain a lists of list
            for key,value in canteen_data.items():
                canteen_loc.append([key,value[0]]) # fills the canteen_loc with a list containing canteen name in index 0 and the location on map in index 1
            # sorts the canteens based on distance, [0] will extract the nearest canteen
            # and returns a list containing data about nearest canteen in the following format: [canteen name, location , distance]
            nearest_canteen=sort_distance(user_location,canteen_loc)[0] # sorts the canteens based on distance and returns list with [canteen name, location , distance]
            print("Based on the distance, the nearest F&B outlet we recommend will be " + nearest_canteen[0]) # tells user the nearest canteen

            #asks the user if he wants to see the destination on the map with error checking
            dest_display = input("Would you like to view the destination on the map (yes or no)? ")
            while dest_display.lower() not in ['yes','no']:
                dest_display = input("Invalid Input. Would you like to view the destination on the map (yes or no)? ")

            # displays the nearest location on the map in green and the user location in cyan
            if dest_display.lower()=='yes':
                dest_displayer(nearest_canteen[0],user_location,nearest_canteen[1])
            

        elif 400<=choice[1]<=540 and 541<=choice[0]<=868: # User clicks on Price
            repeater='chosen' # changes the repeater variable to indicate the user has chosen a choice
            pygame.display.quit() # close window to bring user to python terminal
            print()
            # this block gets the user input for the price range
            print("We will now find a canteen with an average price within your budget.")
            lprice_str = input("Enter the lower limit of your budget: ")
            lprice = get_right_input(lprice_str)
            uprice_str = input("Enter the upper limit of your budget: ")
            uprice = get_right_input(uprice_str)
            while lprice>uprice: # if user inputs a lower limit greater than upper limit which should not be valid
                print("Error: lower limit greater than upper limit")
                lprice_str = input("Enter the lower limit of your budget: ")
                lprice = get_right_input(lprice_str)
                uprice_str = input("Enter the upper limit of your budget: ")
                uprice = get_right_input(uprice_str)
            print()
            price = (lprice,uprice)
            
            pricelist_canteens = [] # will contain list of lists
            for key,value in canteen_data.items():
                pricelist_canteens.append([key, value[1], value[-2]]) # builds a list of lists where each inner list = [canteen name,price of each food, corresponding name of each food]
        
            canteen_dict=search_by_price(price,pricelist_canteens)
            if canteen_dict == {}: # none of the food prices fits the price range of user 
                print("Your search has failed, no canteen with such average price.")
            else: # There are food falling into the criteria of the user, prints the canteen stalls and the food which falls within search criteria
                print("Based on your budget limits, here are some food outlets and food we recommend: ")
                for canteen,food in canteen_dict.items():
                    print('{:30}'.format(canteen),food)
                print()
                #asks the user if he wants to see the destination on the map with error checking
                dest_display = input("Would you like to view the destination on the map (yes or no)? ")
                while dest_display.lower() not in ['yes','no']:
                    dest_display = input("Invalid Input. Would you like to view the destination on the map (yes or no)? ")
                if dest_display.lower()=='yes':
                    canteen_name_lower = []
                    for key in canteen_dict.keys():
                        canteen_name_lower.append(key.lower())
                    canteen_name=input("Please input name of food outlet you will like to visit: ")
                    while canteen_name.lower() not in canteen_name_lower:
                        canteen_name=input("Invalid Input. Please input name of food outlet you will like to visit: ")
                    for key,value in canteen_data.items():
                        if key.lower()==canteen_name.lower():
                            canteen_name=key
                            canteen_loc=value[0]
                    screen = pygame.display.set_mode((1400,750)) # sets size of window
                    user_location=get_user_location() # gets user location
                    if user_location == (None,None): # user clicks on the close button of the window
                        break # if user clicks on the close button of the window, allows the program to end without any errors
                    draw_circle(screen,user_location) # draws a cyan circle on where user is at
                    pygame.display.quit() # closes window
                    dest_displayer(canteen_name,user_location,canteen_loc)            


        elif 400<=choice[1]<=540 and 1035<=choice[0]<= 1362: # User clicks on Food Category
            repeater='chosen' # changes the repeater variable to indicate the user has chosen a choice
        
            pygame.display.quit() # close window to bring user to python terminal

            # This block informs the user the types of food available in NTU so that he knows what to input.
            print()
            print("Currently, we have the following types of food in NTU: ")
            print()
            for i in total_foodlist:
                print(i.lower())
            print()

            # This block asks the user what food he wants and does an error check to ensure he chooses an available item
            user_food=input("Please type your desired food category: ")
            while user_food.lower() not in total_foodlist:
                user_food=input("Your input is invalid. Please type your desired food category: ")
            
            # forms a list of lists where each inner list = [canteen name, types of food, rank of canteen]
            canteen_food=[]
            for key,value in canteen_data.items():
                canteen_food.append([key,value[3],value[-1]])

            # searches all canteen to return canteen with wanted food
            canteen_food=search_by_food(user_food.lower(),canteen_food)
            print("The food outlets with the food of choice are:")
            print()
            for i in canteen_food:
                print(i[0])
            print()
            
            # asks user if he would like a recommendation by distance or rank
            user_choice=input("Would you want to get a recommendation by distance or rank (distance, rank or no)? ")
            while user_choice.lower() not in ['distance','rank','no']:
                user_choice=input("Invalid input.\nWould you want to get a recommendation by distance or rank (distance, rank or no)?")
            print()
            # if user chooses rank
            if user_choice.lower()=='rank':
                # sort the canteen_food according to rankings
                canteen_food=sort_by_rank(canteen_food) # displays a ranked list of canteens with the food indicated by the user and returns the list

                # tells the user which is the best ranked canteen and asks if he would like to see it on the map
                print("The best ranked food outlet is:", canteen_food[0][0])
                print()
                #asks the user if he wants to see the destination on the map with error checking
                dest_display = input("Would you like to view the destination on the map (yes or no)? ")
                while dest_display.lower() not in ['yes','no']:
                    dest_display = input("Invalid Input. Would you like to view the destination on the map (yes or no)? ")
                # if user chooses yes, asks the user for his location and shows the location of the best ranked canteen and the user's current location
                if dest_display.lower()=='yes':
                    screen = pygame.display.set_mode((1400,750))
                    user_location=get_user_location()
                    if user_location == (None,None): # user clicks on the close button of the window
                        break # if user clicks on the close button of the window, allows the program to end without any errors
                    draw_circle(screen,user_location)
                    pygame.display.quit()
                    dest_displayer(canteen_food[0][0],user_location,canteen_data[canteen_food[0][0]][0])
                    
            # if user wants a recommendation by distance
            elif user_choice.lower()=='distance':
                screen = pygame.display.set_mode((1400,750)) # sets size of window
                user_location=get_user_location() # gets user location
                if user_location == (None,None): # user clicks on the close button of the window
                    break # if user clicks on the close button of the window, allows the program to end without any errors
                draw_circle(screen,user_location) # draws a cyan circle on where user is at
                pygame.display.quit() # closes window

                # creates a list of lists where each list = [canteen name, canteen location]
                canteen_loc=[]
                for i in canteen_food:
                    canteen_loc.append([i[0],canteen_data[i[0]][0]])
                nearest_canteen=sort_distance(user_location,canteen_loc)[0] # sorts the canteens based on distance and returns list with [canteen name, location , distance]

                # tells the user which is the nearest canteen with the food chosen by user and asks if he would like to see it on the map
                print("The nearest food outlet is:", nearest_canteen[0])
                print()
                #asks the user if he wants to see the destination on the map with error checking
                dest_display = input("Would you like to view the destination on the map (yes or no)? ")
                while dest_display.lower() not in ['yes','no']:
                    dest_display = input("Invalid Input. Would you like to view the destination on the map (yes or no)? ")
                # if user chooses yes shows the location of the nearest canteen with food chosen by user and the user's current location
                if dest_display.lower()=='yes':    
                    dest_displayer(nearest_canteen[0],user_location,nearest_canteen[1])

        # this block is used to check if the user wants to continue using the recommender. if the user does not wish to continue, it will close the program
        while repeater.lower() not in ['yes','no','not chosen']:
            print()
            repeater=input("Would you like to continue using the F&B recommender(yes or no)? ")
            if repeater.lower()=='no':
                pygame.quit()
                running=False


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()

