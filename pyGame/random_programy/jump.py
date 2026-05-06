# import pygame module in this program 
import pygame
 
# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init()
 
# create the display surface object 
# of specific dimension..e(500, 500). 
win = pygame.display.set_mode((500, 500))
 
# set the pygame window name 
pygame.display.set_caption("Jump Game")
 
# object current co-ordinates
x = 200
y = 200
 
# dimensions of the object
width = 30
height = 40
 
# Stores if player is jumping or not
isjump = False
 
# Force (v) up and mass m.
v = 5
m = 1

vel = 10
# Indicates pygame is running
run = True
 
# infinite loop
while run:
 
    # completely fill the surface object 
    # with black colour 
    win.fill((0, 0, 0))
 
    # drawing object on screen which is rectangle here 
    ctverec=pygame.Rect((255, 0, 0), (x, y, width, height))
    cara1=pygame.Rect(100,200+height,250,2)
    cara2=pygame.Rect(100,200+height*3,300,2)

     
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get():
         
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT:
             
            # it will make exit the while loop
            run = False
   


    

    keys = pygame.key.get_pressed()
        # stores keys pressed  


    # if left arrow key is pressed 
    if keys[pygame.K_LEFT] and x > 0:
        # decrement in x co-ordinate
        x -= vel

        # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x < 500 - width:
        # increment in x co-ordinate
        x += vel
      
    if isjump == False:
 
        # if space bar is pressed
        if keys[pygame.K_SPACE]:
                
            # make isjump equal to True
            isjump = True
             
    if isjump :
        # calculate force (F). F = 1 / 2 * mass * velocity ^ 2.
        F =(1 / 2)*m*(v**2)
         
        # change in the y co-ordinate
        ctverec.y-= 2*F
         
        # decreasing velocity while going up and become negative while coming down
        v = v-1
         
        # object reached its maximum height
        if v<0:
              
            m =-1
            # objected reaches line and stops
            if cara1.colliderect(ctverec):
                isjump = False
                v = 7 - 1
                m = 1
                ctverec.bottom = cara1.top + 1
            if cara2.colliderect(ctverec):
                isjump = False
                v = 7 - 1
                m = 1
                ctverec.bottom = cara2.top + 1
        # objected reaches its original state
        if v ==-6:
 
            # making isjump equal to false 
            isjump = False

   
            # setting original values to v and m
            v = 5
            m = 1
     
    # creates time delay of 10ms
    pygame.time.delay(50)
 
    # it refreshes the window
    pygame.display.update() 
# closes the pygame window    
pygame.quit()