import pygame, sys, math, random
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Lives = 3")
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()
 
angle_P = 0
def angle():
    global angle_P
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        angle_P -= 1.5
    elif keys[pygame.K_d] and not keys[pygame.K_a]:
        angle_P += 1.5
    else:
        angle_P += 0
    return math.radians(angle_P)
def rotate_P(x, y, theta_P):
    return (
        x * math.cos(theta_P) - y * math.sin(theta_P),
        x * math.sin(theta_P) + y * math.cos(theta_P)
    )
def inverse_rotate_P_O(x, y, theta_P):
    return (
        round(x * math.cos(theta_P) + y * math.sin(theta_P), 10),
        round(-x * math.sin(theta_P) + y * math.cos(theta_P), 10)
    )
a_O = 1
pos_x_P = 400
pos_y_P = 300
v_x_P = 0.0
v_y_P = 0.0
a_P = 0.03
def translate_P(x, y):
    return (pos_x_P + x), (pos_y_P + y)
 
def bod_x(x):
    if x > 800:
        x += -800
    elif x < 0:
        x += 800
    return x
def bod_y(y):
    if y > 600:
        y += -600
    elif y < 0:
        y += 600
    return y
 
def collide_P_O(i, j):
    if j < 0.3 * i + 9 and j > -0.3 * i - 9:
        if j < 1.2 * i and j > -1.2 * i:
            return False
        else:
            return True
    else:
        return False
def point_distance_P_O(i, j, x_1, x_2, y_1, y_2):
    run_P = x_2 - x_1
    rise_P = y_2 - y_1
    if run_P == 0 and rise_P == 0:
        return math.hypot(i - x_1, j - y_1)
    t = ((i - x_1) * run_P + (j - y_1) * rise_P) / (run_P ** 2 + rise_P ** 2)
    t = max(0.0, min(1.0, t))
    nx = x_1 + t * run_P
    ny = y_1 + t * rise_P
    return math.hypot(i - nx, j - ny)
def hit_P(i, j, radius):
    i = i - pos_x_P
    j = j - pos_y_P
    (i, j) = inverse_rotate_P_O(i, j, theta_P)
    vertices = [
        (-30, 0),
        (10, 12),
        (0, 0),
        (10, -12)
    ]
    if collide_P_O(i, j) == True:
        return True
    num_vertices = len(vertices)
    for k in range(num_vertices):
        x_1_P, y_1_P = vertices[k]
        x_2_P, y_2_P = vertices[(k + 1) % num_vertices]
        if point_distance_P_O(i, j, x_1_P, y_1_P, x_2_P, y_2_P) <= radius:
            return True
    return False        
def hit_O(x, y, i, j, radius):
    if (x - i) ** 2 + (y - j) ** 2 == radius ** 2:
        return True
    else:
        return False
 
def random_v_O(x):
    return x * random.uniform(0.7, 1.3)
def random_angle_O(x):
    if x == "null":
        return random.uniform(0, 2 * math.pi)
    else:
        return x + random.uniform(-0.125, 0.125)
def random_pos_P_O():
    item = random.randint(0, 800), random.randint(0, 600)
    if (item[0] - pos_x_P) ** 2 + (item[1] - pos_y_P) ** 2 >= 50:
        return item[0] + 200, item[1] + 200
    else:
        return item
 
asteroids_O = [[10, 10, 10, 40, 1], [20, 20, 20, 40, 1], [30, 30, 30, 40, 1]]
asteroids_number_O = 3
destroyed_asteroids_O = []
bullets_P = []
was_colliding = False
lives_P = 3
points_P = 0
add_life_P = 25
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break
    theta_P = angle()    
    if keys[pygame.K_w]:
        v_x_P -= math.cos(theta_P) * a_P
        v_y_P -= math.sin(theta_P) * a_P
    v_x_P *= 0.99
    v_y_P *= 0.99
    pos_x_P += v_x_P
    pos_y_P += v_y_P
    pos_x_P = bod_x(pos_x_P)
    pos_y_P = bod_y(pos_y_P)
   
    is_SPACE = keys[pygame.K_SPACE]
    if keys[pygame.K_SPACE]:
        Colour = (255, 0, 0)
    else:
        Colour = (225, 225, 225)
    if is_SPACE and not was_SPACE:
        bullets_P.append([pos_x_P + math.cos(theta_P + math.pi) * 40, pos_y_P + math.sin(theta_P + math.pi) * 40, v_x_P, v_y_P, theta_P, 0])
    elif keys[pygame.K_c]:
        bullets_P.clear()
    was_SPACE = is_SPACE    
    bullets_P = [[a, b, c, d, e, f] for a, b, c, d, e, f in bullets_P if f < 270]
    bullets_P = [[bod_x(a + math.cos(e + math.pi) + c), bod_y(b + math.sin(e + math.pi) + d), c, d, e, f + 1] for a, b, c, d, e, f in bullets_P]
    asteroids_O = [[bod_x(a + math.cos(c) * e * 0.75), bod_y(b + math.sin(c) * e * 0.75), c, d, e] for a, b, c, d, e in asteroids_O]
    if len(asteroids_O) == 0:
        asteroids_number_O += 1
        for _ in range(asteroids_number_O):
            asteroids_O.append([*random_pos_P_O(), random_angle_O("null"), 40, 1])
   
    destroyed_asteroids_O = set()
    destroyed_bullets_P = set()
    for a, item_a in enumerate(asteroids_O):
        for b, item_b in enumerate(bullets_P):
            if a in destroyed_asteroids_O and b in destroyed_bullets_P:
                continue    
            if (item_a[3] + 2.5) ** 2 >= (item_b[0] - item_a[0]) ** 2 + (item_b[1] - item_a[1]) ** 2 and item_a[3] == 10:
                destroyed_asteroids_O.add(a)
                destroyed_bullets_P.add(b)
                points_P += 1
            elif (item_a[3] + 2.5) ** 2 >= (item_b[0] - item_a[0]) ** 2 + (item_b[1] - item_a[1]) ** 2 and item_a[3] != 10:
                destroyed_asteroids_O.add(a)
                destroyed_bullets_P.add(b)
                points_P += 1
                asteroids_O.append([item_a[0], item_a[1], random_angle_O(item_a[2] + 1), item_a[3] / 2, random_v_O(item_a[4])])  
                asteroids_O.append([item_a[0], item_a[1], random_angle_O(item_a[2] + 1), item_a[3] / 2, random_v_O(item_a[4])])  
    asteroids_O = [item for idx, item in enumerate(asteroids_O) if idx not in destroyed_asteroids_O]
    bullets_P = [item for idx, item in enumerate(bullets_P) if idx not in destroyed_bullets_P]
   
    is_colliding = False
    for item in asteroids_O:
        if hit_P(item[0], item[1], item[3]) == True:
            is_colliding = True
    if is_colliding and not was_colliding:
        lives_P -= 1
        angle_P = 0
        pos_x_P = 400
        pos_y_P = 300
        v_x_P = 0
        v_y_P = 0
    pygame.display.set_caption(f"Lives = {lives_P}, Points = {points_P * 400}")
    was_colliding = is_colliding
    if lives_P < 1:
        angle_P = 0
        v_x_P = 0
        v_y_P = 0
        pos_x_P = 400
        pos_y_P = 300
        asteroids_number_O = 3
        add_life_P = 25
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        lives_P = 3
                        points_P = 0
                        add_life_P = 25
                        paused = False
        asteroids_O = [[*random_pos_P_O(), random_angle_O("null"), 40, 1], [*random_pos_P_O(), random_angle_O("null"), 40, 1], [*random_pos_P_O(), random_angle_O("null"), 40, 1]]
        bullets_P = []
        Colour = (255, 255, 255)
        pygame.display.set_caption("No more lives. Play again?")
    while points_P >= add_life_P:
        lives_P += 1
        add_life_P += 25
               
    player = [translate_P(*rotate_P(-30, 0, theta_P)), translate_P(*rotate_P(10, 12, theta_P)), translate_P(*rotate_P(0, 0, theta_P)), translate_P(*rotate_P(10, -12, theta_P))]
   
    for item in asteroids_O:
        pygame.draw.circle(screen, (255, 255, 255), (item[0], item[1]), item[3])
    for item in bullets_P:
        pygame.draw.circle(screen, (255, 0, 0), (item[0], item[1]), 5)
    pygame.draw.polygon(screen, Colour, player)  
    pygame.display.update()  
    clock.tick(200)