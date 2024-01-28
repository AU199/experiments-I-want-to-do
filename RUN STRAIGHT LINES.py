import pygame 
import math as m

pygame.init()

start_pos = (0,0)
end_pos = (0,0)

all_runs = ["straight", (100,200),(490,50)]
tick = 1000

corner_coordinates = [
    (450, 27),
    (382, 48),
    (351, 81),
    (322, 117),
    (263, 128),
    (225, 71),
    (194, 37),
    (163, 38),
    (142, 56),
    (126, 89),
    (103, 141),
    (98, 182),
    (101, 199),
    (118, 214),
    (147, 221),
    (174, 207),
    (207, 207),
    (220, 223),
    (224, 242),
    (215, 262),
    (113, 382),
    (102, 402),
    (103, 422),
    (123, 442),
    (309, 594),
    (330, 597),
    (356, 588),
    (556, 451),
    (530, 432),
    (542, 398),
    (576, 393),
    (595, 406),
    (615, 426),
    (652, 433),
    (671, 415),
    (679, 130)
]


def car_calc(dir,start_pos,e_p, c_r):
    sp = start_pos
    ep = e_p
    curr_pos = c_r
    g = []
    sim_car = curr_pos
        
    move = (sp[0]-ep[0])*-1
    rise = (sp[1]-ep[1])*-1

    if move != 0:
        slope = (((ep[1]-sp[1])*-1)/((ep[0]-sp[0])*-1))

    slope = ep[0]

    curr_pos = start_pos
    x = curr_pos[0]
    y = curr_pos[1]


    for i in range(1000):
        x = ((1- ((i+1)/1000))*curr_pos[0]) + end_pos[0]*((i+1)/1000)
        if slope != 0:
             y = ((1- ((i+1)/1000))*sp[1]) + ep[1]*((i+1)/1000)
        else:
            y = 0

        g.append((x,y))
        print(sp, ep)

    return g
    
y_changes = []
x_changes = []
gig = []
interpolation_factor = -500

for a in range(1000):
    y_changes.append(interpolation_factor)
    x_changes.append(interpolation_factor)
    interpolation_factor += 1


WIDTH = HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH,HEIGHT))

run = True
index = 0
direction = all_runs[index]
curr_pos = corner_coordinates[index]
end_pos = corner_coordinates[index+1]
car_pos = curr_pos
print("dir", direction,"curr_pos" , curr_pos,"end_pos", end_pos)
while run:
    gig = []
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
           run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            end_pos = pygame.mouse.get_pos()
    screen.fill((0,0,0))

    if curr_pos == end_pos:
        if index < len(all_runs)-2:
            index += 1
        else:
            curr_pos = all_runs[index+1]

    else:
        for i in range(len(corner_coordinates)-1):
            
            pygame.draw.circle(screen,(255,0,0),corner_coordinates[i],5)
            pygame.draw.circle(screen,(255,0,0),corner_coordinates[i+1],5)
            
            if i == 0:
                
                a = car_calc(direction,corner_coordinates[i], corner_coordinates[i+1], curr_pos)
                pygame.draw.line(screen,(0,255,0),(corner_coordinates[i]),corner_coordinates[i+1],4)
                for i in range(len(a)):
                    pygame.draw.circle(screen,(233,0,0),a[i],5)
            
            
            for g in range(len(a)):
                gig.append(a[g])
        
        print(len(gig))
        print(gig[3])
        for g in range(len(gig)):
                pygame.draw.circle(screen,(0,0,255),gig[i],1)
    
    if car_pos != end_pos:
        g = car_pos
    
        

    pygame.draw.circle(screen,(0,255,0),all_runs[index+1],5)


    pygame.display.flip()