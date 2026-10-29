import pygame
import sys
import random


pygame.init()


clock = pygame.time.Clock()
FPS = 60


# THINGS TO MESS AROUND WITH
grid_size = 40
speed = 2 # lower is faster
monster_speed_mult = 3 # monster moves _ times slower than player
max_apples = 3
open_world_mode = True
twoP = True
shooterspawn = False
shooterspawncd = 5 * FPS
monsterspawn = True
monsterspawncd = 3 * FPS
snake_starting_length = 3


# Creating the screen
base_screen_width = 600
margins = 10
sidebar_size = 40
space_size = base_screen_width//grid_size
SCREEN_WIDTH = base_screen_width + margins*2 + (grid_size-1)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH + sidebar_size))
pygame.display.set_caption("Snake+")
game_state = 'startscreen'


hover = None
tick_no = 0
real_tick_no = 0
grid = []
snakes = []
bullets = []
shooters = []
monsters = []
apple_positions = []
direction = 1
score = 0
monsters_eaten = 0
apples_eaten = 0


# Colors (R, G, B)
BG_COLOUR = (30, 30, 40)
BUTTON_COLOUR = (40, 40, 50)
GRID_COLOUR = (40, 40, 50)
HEAD_COLOUR = (125, 150, 255)
PLAYER_COLOUR = (75, 100, 255)
APPLE_COLOUR = (255, 50, 50)
ENEMY_COLOUR = (237, 157, 36)
DEAD_COLOUR = (127, 127, 127)
font = pygame.font.SysFont('arial', 25)




class Button(pygame.Rect):
    def __init__(self, left, top, width, height, text=""):
        super().__init__(left, top, width, height)
        self.text = text




class Snake():
    def __init__(self, startpos, length=snake_starting_length):
        self.length = length
        self.direction = 1 # 1 is right, 2 is down, 3 is left, 4 is up
        self.body = []
        self.dead = False
        snakes.append(self)


        for i in range(length):
            if i == 0:
                self.body.append(SnakeSeg(startpos, i, front=True))
            else:
                self.body.append(SnakeSeg(startpos, i))
        self.head = self.body[0]


    def advance(self, gridsizex, gridsizey, openworldmode=open_world_mode):
        for segment in self.body:
            if segment.rank == 0: # head
                global direction
                if self.direction == 1:
                    nextpos = (segment.x + 1, segment.y)
                    direction = 1
                elif self.direction == 2:
                    nextpos = (segment.x, segment.y + 1)
                    direction = 2
                elif self.direction == 3:
                    nextpos = (segment.x - 1, segment.y)
                    direction = 3
                elif self.direction == 4:
                    nextpos = (segment.x, segment.y - 1)
                    direction = 4  


                next_x, next_y = nextpos[0], nextpos[1]


                if 0 <= next_x <= gridsizex-1 and 0 <= next_y <= gridsizey-1:
                    if (grid[next_y][next_x].filled == 'empty' or grid[next_y][next_x].filled == 'apple' or grid[next_y][next_x].filled == 'monster') and not self.dead:
                        self.head.move(nextpos)
                        if grid[next_y][next_x].filled == 'apple':
                            self.grow()
                            global score, apples_eaten
                            score += 1
                            apples_eaten += 1
                            apple_positions.remove((next_x, next_y))
                    elif self.dead == False:
                        self.die() # CRASHING
                        break
                else:
                    if open_world_mode:
                        if next_x < 0:
                            next_x = gridsizex-1
                        elif next_x > gridsizex-1:
                            next_x = 0
                        if next_y < 0:
                            next_y = gridsizey-1
                        elif next_y > gridsizey-1:
                            next_y = 0


                        self.head.move((next_x, next_y))
                    elif self.dead == False:
                        self.die() # EXITING BOUNDS
                        break


            elif segment.pos != self.body[segment.rank-1].pos:
                    if not self.dead:
                        segment.move(self.body[segment.rank-1].previouspos)


    def grow(self):
        self.body.append(SnakeSeg(self.body[-1].pos, self.length))
        self.length += 1


    def shrink(self):
        self.body.pop()
        self.length -= 1


    def die(self):
        self.dead = True
        print("Score:", self.length)




class SnakeSeg():
    def __init__(self, pos, rank, front=False):
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.previouspos = pos
        self.rank = rank
        if self.rank == 0:
            self.head = True
        else:
            self.head = False
        self.front = front


    def move(self, next_pos):
        self.previouspos = self.pos
        self.pos = next_pos
        self.x = self.pos[0]
        self.y = self.pos[1]


    def split(self, parent):
        for i in range(parent.length - self.rank):
            parent.shrink()




class Gridspace():
    def __init__(self, x, y, spacesize, margin):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.left = margin + (spacesize+1)*self.x
        self.top = margin + (spacesize+1)*self.y
        self.width = spacesize
        self.height = spacesize
        self.filled = "empty"


    def ref_rect(self):
        return (self.left, self.top, self.width, self.height)


    def center(self):
        return (self.left + self.width/2, self.top + self.height/2)


    def drawself(self, surface, spacesize: int, colour=GRID_COLOUR, apple_colour=APPLE_COLOUR, snake_body_colour=PLAYER_COLOUR, snake_head_colour=HEAD_COLOUR, dead_snake_colour=DEAD_COLOUR, bullet_colour=ENEMY_COLOUR):
        if self.filled == 'snake body':
            pygame.draw.rect(surface, snake_body_colour, self.ref_rect())
        elif self.filled == 'snake head':
            pygame.draw.rect(surface, snake_head_colour, self.ref_rect())
        elif self.filled == 'dead snake':
            pygame.draw.rect(surface, dead_snake_colour, self.ref_rect())
        elif self.filled == 'monster':
            pygame.draw.rect(surface, bullet_colour, self.ref_rect())
        else:
            pygame.draw.rect(surface, colour, self.ref_rect())
            if self.filled == 'bullet':
                pygame.draw.circle(surface, bullet_colour, self.center(), (spacesize//3+1))
            if self.filled == 'apple':
                pygame.draw.circle(surface, apple_colour, self.center(), spacesize//3+1)




class Bullet():
    def __init__(self, dir, pos):
        self.dir = dir
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        bullets.append(self)


    def move(self, gridsizex=grid_size, gridsizey=grid_size):
        if self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y += 1
        elif self.dir == 3:
            self.x -= 1
        elif self.dir == 4:
            self.y -= 1


        if 0 <= self.x <= gridsizex and 0 <= self.y <= gridsizey:
            self.pos = (self.x, self.y)
        else:
            bullets.remove(self)




class Shooter():
    def __init__(self, dir, pos, cd=120):
        self.dir = dir
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.cd = cd
        self.wind = cd
        shooters.append(self)


    def shoot(self):
        bullet = Bullet(self.dir, self.pos)




class Monster():
    def __init__(self, pos, attribute=None):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.attribute = attribute
        if self.attribute == None:
            self.attribute = random.choice(['angry', 'hungry'])
        monsters.append(self)


    def move(self, movement_type, targetpos=[None, None], gridsizex=grid_size, gridsizey=grid_size):
        targetx = targetpos[0]
        targety = targetpos[1]
        possible_dirs = []
        if movement_type == 'random':
            if self.x < gridsizex-1:
                possible_dirs.append(1)
            if self.y < gridsizey-1:
                possible_dirs.append(2)
            if self.x > 0:
                possible_dirs.append(3)
            if self.y > 0:
                possible_dirs.append(4)


        elif movement_type == 'targetted':
            if self.x > targetx:
                possible_dirs.append(3)
            elif self.x < targetx:
                possible_dirs.append(1)
            elif self.y > targety:
                possible_dirs.append(4)
            elif self.y < targety:
                possible_dirs.append(2)
       
        try:
            self.dir = random.choice(possible_dirs)
            if self.dir == 1:
                self.x += 1
            elif self.dir == 2:
                self.y += 1
            elif self.dir == 3:
                self.x -= 1
            elif self.dir == 4:
                self.y -= 1
            self.pos = (self.x, self.y)
            if self.pos in apple_positions:
                summon_monster(grid, pos=self.pos)
                apple_positions.remove(self.pos)
        except:
            pass




def count_grid(grid, target):
    endlist = []
    for row in grid:
        for space in row:
            if space.filled == target:
                endlist.append(space)
    return endlist


def get_closest(target_pos, positions):
    closest = -1
    closet_index = -1
    for index, position in enumerate(positions):
        if closest == -1 or closest > abs(target_pos[0] - position[0]) + abs(target_pos[1] - position[1]):
            closest = abs(target_pos[0] - position[0]) + abs(target_pos[1] - position[1])
            closet_index = index
    try:
        return positions[closet_index]
    except:
        if len(positions) > 0:
            return positions[-1]
        else:
            return (0, 0)
   
def spawn_apple(grid):
    empty_spots = count_grid(grid, 'empty')
    if len(empty_spots) > 0:
        choice = random.randint(0, len(empty_spots)-1)
        empty_spots[choice].filled = 'apple'
        apple_positions.append((empty_spots[choice].pos))


def summon_monster(grid, pos=(None, None)):
    if pos == (None, None):
        try:
            Monster(random.choice(count_grid(grid, 'empty')).pos)
        except IndexError:
            Monster(random.choice(count_grid(grid, 'apple')).pos)
    else:
        Monster(pos)
    global score
    score -= 2


def summon_shooter(cooldown=20):
    shooter_dir = random.randint(1, 4)
    if shooter_dir == 1:
        s = Shooter(shooter_dir, (0, random.randint(0, grid_size-1)), cd=cooldown)
    elif shooter_dir == 2:
        s = Shooter(shooter_dir, (random.randint(0, grid_size-1), 0), cd=cooldown)
    elif shooter_dir == 3:
        s = Shooter(shooter_dir, (grid_size-1, random.randint(0, grid_size-1)), cd=cooldown)
    elif shooter_dir == 4:
        s = Shooter(shooter_dir, (random.randint(0, grid_size-1), grid_size-1), cd=cooldown)


def initgame(monster=monsterspawn, shooter=shooterspawn, gridsize=grid_size):
    if monster:
        summon_monster(grid)
    if shooter:
        summon_shooter()


button_width = (SCREEN_WIDTH-(4*margins))//3
button_height = (SCREEN_WIDTH-(2*margins))//3


howtoplay = Button(margins, margins+button_height, button_width, button_height)
play = Button(margins*2 + button_width, margins+button_height, button_width, button_height)
settings = Button(margins*3 + 2* button_width, margins+button_height, button_width, button_height)


# creating the grid
for i in range(grid_size): #rows
    grid.append([])
    for ii in range(grid_size): # columns
        grid[i].append(Gridspace(ii, i, space_size, margins))


p1 = Snake((1, 3))
if twoP:
    p2 = Snake((1, 10))


while True:
    screen.fill(BG_COLOUR)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_state = 'startscreen'
                score = 0
                tick_no = 0
                monsters_eaten = 0
                apples_eaten = 0
                snakes.clear()
                monsters.clear()
                shooters.clear()
            if game_state == 'ingame':
                if not twoP:
                    if (event.key == pygame.K_d or event.key == pygame.K_RIGHT) and direction != 3:
                        for snake in snakes:
                            snake.direction = 1
                    elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and direction != 4:
                        for snake in snakes:
                            snake.direction = 2
                    elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and direction != 1:
                        for snake in snakes:
                            snake.direction = 3
                    elif (event.key == pygame.K_w or event.key == pygame.K_UP) and direction != 2:
                        for snake in snakes:
                            snake.direction = 4
               
                elif twoP:
                    if event.key == pygame.K_d and p1.direction != 3:
                        p1.direction = 1
                    elif event.key == pygame.K_s and p1.direction != 4:
                        p1.direction = 2
                    elif event.key == pygame.K_a and p1.direction != 1:
                        p1.direction = 3
                    elif event.key == pygame.K_w and p1.direction != 2:
                        p1.direction = 4


                    if event.key == pygame.K_RIGHT and p2.direction != 3:
                        p2.direction = 1
                    elif event.key == pygame.K_DOWN and p2.direction != 4:
                        p2.direction = 2
                    elif event.key == pygame.K_LEFT and p2.direction != 1:
                        p2.direction = 3
                    elif event.key == pygame.K_UP and p2.direction != 2:
                        p2.direction = 4


                if event.key == pygame.K_r and len(snakes) == 0:
                    tick_no = 0
                    score = 0
                    monsters_eaten = 0
                    apples_eaten = 0
                    snakes.clear()
                    monsters.clear()
                    shooters.clear()
                    p1 = Snake((1, 3))
                    if twoP:
                        p2 = Snake((1, 10))


        elif event.type == pygame.MOUSEBUTTONUP:
            if game_state == 'startscreen':
                if play.collidepoint(event.pos):
                    game_state = 'ingame'
                    tick_no = 0
                    score = 0


        elif event.type == pygame.MOUSEMOTION:
            if game_state == 'startscreen':
                '''if howtoplay.collidepoint(event.pos):
                    hover = 'How to Play'''
                if play.collidepoint(event.pos):
                    hover = "Play"
                    '''elif settings.collidepoint(event.pos):
                        hover = "Settings"'''
                else:
                    hover = ''


    scoreboard = font.render(f'Score / EnemiesAlive / EnemiesEaten / ApplesEaten: {score} / {len(monsters)} / {monsters_eaten} / {apples_eaten}', True, HEAD_COLOUR)
    scoreboard_rect = scoreboard.get_rect()
    scoreboard_rect.center = (SCREEN_WIDTH//2, SCREEN_WIDTH+sidebar_size//2)
    if game_state == 'startscreen':
        pygame.draw.rect(screen, BG_COLOUR, scoreboard_rect)
        scoreboard = font.render(hover, True, HEAD_COLOUR)
    screen.blit(scoreboard, scoreboard_rect)
   
    if game_state == 'startscreen':
        # pygame.draw.rect(screen, BUTTON_COLOUR, howtoplay)
        pygame.draw.rect(screen, BUTTON_COLOUR, play)
        # pygame.draw.rect(screen, BUTTON_COLOUR, settings)


    if game_state == 'ingame':
        if tick_no % speed == 0:
            for snake in snakes:
                snake.advance(grid_size, grid_size)
            for bullet in bullets:
                bullet.move()


        if tick_no % (speed * monster_speed_mult) == 1:
            for monster in monsters:
                choice = random.randint(1, 2) # 50/50 to move random or to more targetted
                if len(snakes) != 0 and monster.attribute == 'angry' and choice == 1:
                    monster.move('targetted', targetpos=random.choice(snakes).head.pos) # It will target a random snake's head - only really matter if there are >1 snake
                elif monster.attribute == 'hungry' and choice == 1:
                    monster.move('targetted', targetpos=get_closest(monster.pos, apple_positions))
                else:
                    monster.move('random')


        if tick_no % speed == speed//2:
            for bullet in bullets:
                bullet.move()


        if tick_no % speed//2 == 0:
            for shooter in shooters:
                if shooter.wind == 0:
                    shooter.shoot()
                    shooter.wind = shooter.cd
                else:
                    shooter.wind -= 1




        if tick_no % shooterspawncd == 0 and shooterspawn:
            summon_shooter()
        if tick_no % monsterspawncd == 0 and monsterspawn:
            summon_monster(grid)
               


        no_apples = len(count_grid(grid, 'apple'))
        if no_apples < max_apples:
            spawn_apple(grid)


        for snake in snakes:
            if snake.dead and snake.length > 0 and tick_no % speed//2 == 0:
                snake.shrink()
            elif snake.length <= 0:
                snakes.remove(snake)


        for monster in monsters:
            if len(snakes) == 1:
                if snakes[0].length > 1:
                    monster.attribute = 'hungry'
                else:
                    monster.attribute = 'angry'
            elif len(snakes) > 1:
                monster.attribute = random.choice(['hungry', 'angry'])
            else:
                monster.attribute = 'hungry'


        # Draw bg and grid
        for y, row in enumerate(grid): # y
            for x, space in enumerate(row): # x
                if space.filled != 'apple':
                    space.filled = 'empty'


                for bullet in bullets:
                    if bullet.pos == (x, y):
                        space.filled = 'bullet'


                for monster in monsters:
                    if monster.pos == (x, y):
                        space.filled = 'monster'


                for snake in snakes:
                    for snake_seg in snake.body:
                        if snake_seg.pos == (x, y):


                            if snake_seg.front and not snake.dead:
                                space.filled = 'snake head'
                            elif not snake.dead:
                                space.filled = 'snake body'
                            elif snake.dead:
                                space.filled = 'dead snake'


                            for bullet in bullets:
                                if bullet.pos == snake_seg.pos:
                                    snake_seg.split(snake)


                            for monster in monsters:
                                if monster.pos == snake_seg.pos:
                                    if not snake_seg.head:
                                        score -= (snake.length-snake_seg.rank)
                                        snake_seg.split(snake)
                                       
                                    elif snake_seg.head and snake.length > 1:
                                        score += 5
                                        monsters_eaten += 1
                                        monsters.remove(monster)


                                    elif snake_seg.head and snake.length == 1:
                                        snake.die()
                space.drawself(screen, space_size)


    tick_no += 1
    real_tick_no += 1
    clock.tick(FPS)  # Limits the loop to 60 frames per second
    pygame.display.update()





