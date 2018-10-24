## _   _ _________________ ___________   _____ ___________ _____ 
##| | | |  _  | ___ | ___ |_   _|  _  \ /  __ |  _  | ___ |  ___|
##| |_| | | | | |_/ | |_/ / | | | | | | | /  \| | | | |_/ | |__  
##|  _  | | | |    /|    /  | | | | | | | |   | | | |    /|  __| 
##| | | \ \_/ | |\ \| |\ \ _| |_| |/ /  | \__/\ \_/ | |\ \| |___ 
##\_| |_/\___/\_| \_\_| \_|\___/|___/    \____/\___/\_| \_\____/

####
##______ ___________ _____ _____ _____ 
##|  ___|  _  | ___ \  ___/  ___|_   _|
##| |_  | | | | |_/ / |__ \ `--.  | |  
##|  _| | | | |    /|  __| `--. \ | |  
##| |   \ \_/ / |\ \| |___/\__/ / | |  
##\_|    \___/\_| \_\____/\____/  \_/ 
##print("")
##print("")
##print("")
##print("")
##print("")
##print("")
##chosen = "o"
##running = 1
##state= 0
##########################################################
## ADVENTURE GAME STARTS HERE
##########################################################
import random
from adventure import *

# start by creating the game system
game = Game("HORRID CORE")

# define and describe a couple of locations
room = game.new_location(
  "bedroom",
"""
you find yourself playing zork 1
on your computer, your house dead silent around you.

slowly a cough echoes out among the silence, it was not you.
 ▄▄▄▄   ▓█████ ▓█████▄  ██▀███   ▒█████   ▒█████   ███▄ ▄███▓
▓█████▄ ▓█   ▀ ▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒
▒██▒ ▄██▒███   ░██   █▌▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▓██    ▓██░
▒██░█▀  ▒▓█  ▄ ░▓█▄   ▌▒██▀▀█▄  ▒██   ██░▒██   ██░▒██    ▒██ 
░▓█  ▀█▓░▒████▒░▒████▓ ░██▓ ▒██▒░ ████▓▒░░ ████▓▒░▒██▒   ░██▒
░▒▓███▀▒░░ ▒░ ░ ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░   ░  ░
▒░▒   ░  ░ ░  ░ ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░ ░  ░      ░
 ░    ░    ░    ░ ░  ░   ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░      ░   
 ░         ░  ░   ░       ░         ░ ░      ░ ░         ░   
      ░         ░                                            
""")

landing = game.new_location(
  "landing",
"""A small area at the bottom of a flight of stairs.
There is a glass door to the east, and door to the
west. To the north there is a dark muddy hole.
 _       ____  ____   ___    ____  ____    ____     
| |     /    ||    \ |   \  |    ||    \  /    |    
| |    |  o  ||  _  ||    \  |  | |  _  ||   __|    
| |___ |     ||  |  ||  D  | |  | |  |  ||  |  |    
|     ||  _  ||  |  ||     | |  | |  |  ||  |_ |    
|     ||  |  ||  |  ||     | |  | |  |  ||     |    
|_____||__|__||__|__||_____||____||__|__||___,_| 
 """)

office = game.new_location(
  "Office",
"""A nicely organized office.
There is a door to the south.
    ,----..                                                     
   /   /   \      ,---,.    ,---,.   ,---,  ,----..      ,---,. 
  /   .     :   ,'  .' |  ,'  .' |,`--.' | /   /   \   ,'  .' | 
 .   /   ;.  \,---.'   |,---.'   ||   :  :|   :     :,---.'   | 
.   ;   /  ` ;|   |   .'|   |   .':   |  '.   |  ;. /|   |   .' 
;   |  ; \ ; |:   :  :  :   :  :  |   :  |.   ; /--` :   :  |-, 
|   :  | ; | ':   |  |-,:   |  |-,'   '  ;;   | ;    :   |  ;/| 
.   |  ' ' ' :|   :  ;/||   :  ;/||   |  ||   : |    |   :   .' 
'   ;  \; /  ||   |   .'|   |   .''   :  ;.   | '___ |   |  |-, 
 \   \  ',  / '   :  '  '   :  '  |   |  ''   ; : .'|'   :  ;/| 
  ;   :    /  |   |  |  |   |  |  '   :  |'   | '/  :|   |    \ 
   \   \ .'   |   :  \  |   :  \  ;   |.' |   :    / |   :   .' 
    `---`     |   | ,'  |   | ,'  '---'    \   \ .'  |   | ,'   
              `----'    `----'              `---`    `----'     
                                                               """)

tunnel = game.new_location(
  "Tunnel",
"""A dark and moist muddy hole that might lead somewhere...
 ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄▄        ▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄           
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌      ▐░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░▌          
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌     ▐░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          
     ▐░▌     ▐░▌       ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌          ▐░▌          
     ▐░▌     ▐░▌       ▐░▌▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌          
     ▐░▌     ▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌          
     ▐░▌     ▐░▌       ▐░▌▐░▌   ▐░▌ ▐░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌          
     ▐░▌     ▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌    ▐░▌▐░▌▐░▌          ▐░▌          
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌     ▐░▐░▌▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ 
     ▐░▌     ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀""")

closet = game.new_location(
  "closet",
"""A nicely organized storage room, there are jars of food in here, why?, dont ask me, im just the developer.
There is a open vent to the south and  a door to the north.
closet, has food jar
______________________________
|             |              |
|             |              |
|             |              |
|           . | .            |
|             |              |
|             |              |
|             |              |""")

vent = game.new_location(
  "Vent",
"""why are you here?, exit north or backtract please""")

cave = game.new_location(
    "small cave",
    """a little light trickles into the small cave, the air is humid and hard to breath.
       ****       *      *           *    *****
     **          *  *      *        *     *      
     *          *****       *      *      *****
     **       *        *      *   *       *      
       ****  *          *       *         *****""")
forest1 = game.new_location(
  "forest",
"""small oaklands meadow
______ ___________ _____ _____ _____ 
|  ___|  _  | ___ \  ___/  ___|_   _|
| |_  | | | | |_/ / |__ \ `--.  | |  
|  _| | | | |    /|  __| `--. \ | |  
| |   \ \_/ / |\ \| |___/\__/ / | |  
\_|    \___/\_| \_\____/\____/  \_/  
""")
forest2 = game.new_location(
  "forest",
"""small juniper meadow
______ ___________ _____ _____ _____ 
|  ___|  _  | ___ \  ___/  ___|_   _|
| |_  | | | | |_/ / |__ \ `--.  | |  
|  _| | | | |    /|  __| `--. \ | |  
| |   \ \_/ / |\ \| |___/\__/ / | |  
\_|    \___/\_| \_\____/\____/  \_/  """)
forest3 = game.new_location(
  "forest",
"""redwood forest
______ ___________ _____ _____ _____ 
|  ___|  _  | ___ \  ___/  ___|_   _|
| |_  | | | | |_/ / |__ \ `--.  | |  
|  _| | | | |    /|  __| `--. \ | |  
| |   \ \_/ / |\ \| |___/\__/ / | |  
\_|    \___/\_| \_\____/\____/  \_/  """)
forest4 = game.new_location(
  "forest",
"""light clearing, slightly overgrown
______ ___________ _____ _____ _____ 
|  ___|  _  | ___ \  ___/  ___|_   _|
| |_  | | | | |_/ / |__ \ `--.  | |  
|  _| | | | |    /|  __| `--. \ | |  
| |   \ \_/ / |\ \| |___/\__/ / | |  
\_|    \___/\_| \_\____/\____/  \_/  """)
grave = game.new_location(
    "abandoned graveyard", 
"""jagged tombstones rule the area as a light shiver overcomes you
  _______ .______          ___   ____    ____  ___________    ____  ___      .______       _______  
 /  _____||   _  \        /   \  \   \  /   / |   ____\   \  /   / /   \     |   _  \     |       \ 
|  |  __  |  |_)  |      /  ^  \  \   \/   /  |  |__   \   \/   / /  ^  \    |  |_)  |    |  .--.  |
|  | |_ | |      /      /  /_\  \  \      /   |   __|   \_    _/ /  /_\  \   |      /     |  |  |  |
|  |__| | |  |\  \----./  _____  \  \    /    |  |____    |  |  /  _____  \  |  |\  \----.|  '--'  |
 \______| | _| `._____/__/     \__\  \__/     |_______|   |__| /__/     \__\ | _| `._____||_______/""")
balcony = game.new_location(
    "small balcony",
"""the winds whisper by, the noise still continuing
######                                              
#     #     ##     #        ####         
#     #    #  #    #       #                
######    #    #   #      #                 
#     #    ####    #                  
#     #   #    #   #      #                  
######    #    #   ######   ####           """)
rainbow = game.new_location(
  "rainbow",
"""in the forest a clearing comes into view, and on the center of is a rock with a gold coin on it
           _       _                   
          (_)     | |                  
 _ __ __ _ _ _ __ | |__   _____      __
| '__/ _` | | '_ \| '_ \ / _ \ \ /\ / /
| | | (_| | | | | | |_) | (_) \ V  V / 
|_|  \__,_|_|_| |_|_.__/ \___/ \_/\_/  
                                       
                                      """)
hell = game.new_location(
    "HELL",
"""THE SOUNDS OF A TRILLION SCREAMING SOULS CORRUPT YOUR EARS, THE ROARING LAUGHTER OF SATAN OVER TAKING THE AIR
*      *  *****     *        *      
*      *  *         *        *      
 ******   *****     *        *       
*      *  *         *        *        
*      *  *****     *****    *****  
""")    
door = game.new_location(
    "HELL'S DOORSTEP",
"""a great , shiny gate stands before you, ready to let you in, however a odd shaped lock denies you access
 _   _  _____ _      _     _ _____   _____   ___ _____ _____ 
| | | ||  ___| |    | |   ( )  ___| |  __ \ / _ \_   _|  ___|
| |_| || |__ | |    | |   |/\ `--.  | |  \// /_\ \| | | |__  
|  _  ||  __|| |    | |      `--. \ | | __ |  _  || | |  __| 
| | | || |___| |____| |____ /\__/ / | |_\ \| | | || | | |___ 
\_| |_/\____/\_____/\_____/ \____/   \____/\_| |_/\_/ \____/ 
                                                             
                                                            """)
chamber = game.new_location(
    "Satan's chamber",
"""the god of death sits before you, awaiting your first move
        _____         __     __           _____                ___________        ______  ______     _____\    \ ___________       
   _____\    \_      /  \   /  \        /      |_             /           \       \     \|\     \   /    / |    |\          \      
  /     /|     |    /   /| |\   \      /         \           /    _   _    \       |     |\|     | /    /  /___/| \    /\    \     
 /     / /____/|   /   //   \\   \    |     /\    \         /    //   \\    \      |     |/____ / |    |__ |___|/  |   \_\    |    
|     | |____|/   /    \_____/    \   |    |  |    \       /    //     \\    \     |     |\     \ |       \        |      ___/     
|     |  _____   /    /\_____/\    \  |     \/      \     /     \\_____//     \    |     | |     ||     __/ __     |      \  ____  
|\     \|\    \ /    //\_____/\\    \ |\      /\     \   /       \ ___ /       \   |     | |     ||\    \  /  \   /     /\ \/    \ 
| \_____\|    |/____/ |       | \____\| \_____\ \_____\ /________/|   |\________\ /_____/|/_____/|| \____\/    | /_____/ |\______| 
| |     /____/||    | |       | |    || |     | |     ||        | |   | |        ||    |||     | || |    |____/| |     | | |     | 
 \|_____|    |||____|/         \|____| \|_____|\|_____||________|/     \|________||____|/|_____|/  \|____|   | | |_____|/ \|_____| 
        |____|/                                                                                          |___|/                   """)

window = game.new_location("window",
"""a freaking window, what else?""")

game.new_connection("Glass Door", room, landing, [IN, WEST], [OUT, EAST])
game.new_connection("Office Door", landing, office, [IN, WEST], [OUT, EAST])
game.new_connection("Tunnel Opening", landing, tunnel, [DOWN, NORTH], [UP, SOUTH])
game.new_connection("closet", room,closet,[IN, NORTH], [OUT, SOUTH])
game.new_connection("vent", closet,vent,[IN,NORTH], [OUT,SOUTH])
game.new_connection("cave", tunnel, cave, [IN ,NORTH], [OUT ,SOUTH])
game.new_connection("tunnel opening", tunnel, cave, [IN ,NORTH], [OUT ,SOUTH])
game.new_connection("balcony", room,balcony,[IN,SOUTH], [OUT,NORTH])
game.new_connection("forest", balcony,forest1,[IN,SOUTH], [OUT,NORTH])
game.new_connection("graves", forest1,grave,[IN,SOUTH], [OUT,NORTH])
game.new_connection("forest", grave,forest3,[IN,EAST], [OUT,WEST])
game.new_connection("rainbow", forest3,rainbow,[IN,EAST], [OUT,WEST])
game.new_connection("forest", grave,forest4,[IN, SOUTH], [OUT, NORTH])
game.new_connection("forest", grave,forest2,[IN, WEST], [OUT,EAST])
game.new_connection("HELL'S DOORSTEP",cave, door,[IN, NORTH], [OUT, SOUTH])
game.new_connection("HELL",door, hell,[IN, NORTH], [OUT, SOUTH])
game.new_connection("DEATH", hell, chamber, [IN, WEST], [OUT, EAST])
game.new_connection("window",room, window,[IN,EAST],[OUT,WEST])
#game.add_connection("outside",window,forest1,[IN,SOUTH],[OUT,NORTH])
                    
# Now let's add a thing, a key, by providing a single word name and a longer
# description.  We will create the key at the room.
key = room.new_object("key", "a small tarnished key")
pen = room.new_object("pen", "a pen, what did you expect?")
jar= closet.new_object("jar", "food, glorious food")
lint = vent.new_object("lint", "lint, very flammable")
dirt = tunnel.new_object("dirt", "brown loamy soil")
pebble = cave.new_object("pebble", "a smooth round rock, it appears to glow")
ink = office.new_object("ink", "writing ink, tastes bad")
knife = office.new_object("knife", "very sharp, a great weapon")
potato = landing.new_object("potato", "low IQ object")
gold = rainbow.new_object("coin", "a single coin of the finest gold")
crystal = grave.new_object("crystal","a small, white crystal charged with soul remnant, pick up if you dare")
satan= chamber.new_object("satan","the god of death, now in your pocket")
rope = closet.new_object("rope", "a rope in your closet man, whatcha doin?")
# And we can make the key required to open the office
office.make_requirement(key)
hell.make_requirement(crystal)
# Let's add a special phrase. We can attach this phrase to any object, location or actor,
# and the phrase will trigger only if that object or actor is present or at the given location.
key.add_phrase("rub key", game.say("You rub the key, but fail to shine it."))
pen.add_phrase("click pen", game.say("the pen clicked. great"))
jar.add_phrase("eat", game.say("cool, you ate food"))
lint.add_phrase("light lint", game.say("lint lighted"))
pebble.add_phrase("rub pebble",game.say("it began to glow brighter"))
potato.add_phrase("throw potato", game.say("quit throwing down syndrome kids, its bad for your health"))
gold.add_phrase("rub coin", game.say("the light of your heart compels you, +2 luck, +2 melee"))
satan.add_phrase("punch satan", game.say("its not very effective..."))
satan.add_phrase("stab satan", game.say("not really effective"))
satan.add_phrase("kick satan", game.say("still not effective"))
satan.add_phrase("throw potato at satan", game.say("MONSTER KILL"))
rope.add_phrase("commit neck rope", game.say("NIGHTY NIGHT BIATCH"))
player = game.new_player(room)



game.run()


