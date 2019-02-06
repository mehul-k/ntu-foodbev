## width = 1400 height = 750

# This Dictionary contains the name of canteens as its keys and lists of data as its values.
# each key will be the canteen's name while the value of the key will contain a list
# each list = [coordinates of canteen in a tuple ,  tuple containing average price of each food at canteen, a list of tuples of the nearest red and blue line bus stops,
#              list containing the types of food, canteen's ranking]
canteen_data = {"Food Court 1":[(786, 548),(4,5,4.5,2),[(846, 685), (871, 548)], ["chinese", "japanese", "malay", "beverages"],13],
                "Food Court 2":[(866, 447),(4,4.5,5.2,5.5,1.5),[(891, 440), (871, 548)],["chinese", "malay", "italian", "western", "beverages"],6], 
                "Food Court 9":[(1119, 257),(3.5,4.5,5,1.2),[(1066, 323), (1043, 351)],["chinese", "malay", "western", "beverages"],4],
                "Food Court 11":[(1340, 186),(3.7,4,4,4.5,1.3),[(1344, 240), (1352, 247)], ["chinese", "japanese", "indian", "italian", "beverages"],1],
                "Food Court 13":[(791, 80),(3.2,3.6,3.8,4.5,1),[(770, 56), (920, 46)],["chinese", "malay", "indian", "western", "beverages"],14],
                "Food Court 14":[(943, 90),(4.7,5,4,1.7),[(770, 56), (920, 46)], ["chinese", "japanese", "malay", "beverages"],9],
                "Food Court 16":[(703, 152),(5,4,5,1.6),[(770, 56), (667, 180)],["chinese", "malay", "thai", "beverages"],11],
                "Ananda Kitchen":[(1369, 258),(2.8,5,4,5,1.1),[(1344, 240), (1352, 247)],["chinese", "korean", "indian", "italian", "beverages"],5],
                "Foodgle Food Court":[(1227, 111),(3,4,4,5,1.3),[(1220, 95), (1351, 106)],["chinese", "japanese", "korean", "western", "beverages"],2],
                "North Hill Food Court":[(1393, 282),(3.2,4,4,4,1.1),[(1344, 240), (1352, 247)], ["chinese", "malay", "indian", "western", "beverages"],10],
                "Pioneer Food Court":[(910, 690),(3,4,4,4,4,7,6),[(846, 685), (646, 736)], ["chinese","japanese", "malay", "korean", "indian", "italian", "thai"],7],
                "Quad Cafe":[(254, 338),(4,3.5,4.5,1),[(189, 306), (249, 234)], ["chinese", "malay", "korean", "beverages"],12],
                "North Spine Plaza":[(504, 270),(3.5,5,3.7,4.3,3,5,4.5,1.2),[(536, 238), (513, 225)], ["chinese", "japanese", "malay", "korean", "indian", "italian", "western", "beverages"],8],
                "Koufu @ the South Spine":[(292, 586),(3.3,5.3,3.5,3.7,4.5,1.2),[(357, 649), (345, 680)], ["chinese", "japanese", "malay", "indian", "italian", "beverages"],3]}

# This Dictionary contains the name of the red line bus stops as its keys and the location of the bus stops as its value.
# each key will be the name of the red line bus stop and the value will be a tuple of the bus stop's coordinates on the map
redbus_data = {"LWN Library, Opp. NIE":(536, 238),
               "SBS":(189, 306),
               "WKWSCI":(59, 457),
               "Hall 7":(66, 661),
               "Innovation Centre":(357, 649),
               "Hall 4":(611, 698),
               "Hall 1 (Blk 18)":(846, 685),
               "Food Court 2":(891, 440),
               "Hall 8 & 9":(1066, 323),
               "Hall 11":(1344, 240),
               "Grad Hall 1 & 2":(1395, 138),
               "Nanyang Crescent Hall":(1220, 95),
               "​Hall 12 & 13":(770, 56)}

# This Dictionary contains the name of the blue line bus stops as its keys and the location of the bus stops as its value.
# each key will be the name of the blue line bus stop and the value will be a tuple of the bus stop's coordinates on the map
bluebus_data = {"NIE, Opp. LWN Library":(513, 225),
                "Opp. Hall 3 & 16":(667, 180),
                "Opp. Hall 14 & 15":(920, 46),
                "Opp Nanyang Crescent Hall":(1351, 106),
                "Opp. Hall 10 & 11":(1352, 247),
                "Nanyang Heights, Opp. Hall 8":(1043, 351),
                "Hall 6, Opp. Hall 2":(871, 548),
                "Opp. Hall 4":(646, 736),
                "Opp. Innovation Centre":(345, 680),
                "Opp. SPMS":(172, 571),
                "Opp. WKWSCI":(58, 506),
                "Opp. CEE":(249, 234)}
# list of all the types of food sold in the NTU canteens
total_foodlist=["chinese", "japanese", "malay", "indian", "italian", "beverages","thai","indian","korean","western"]

