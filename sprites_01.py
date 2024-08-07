import pygame
import math
import random
#11122
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Погоня за яблоком')
clock = pygame.time.Clock()

running = True
white = (255, 255, 255)
black = (0, 0, 0)
sound_effect = pygame.mixer.Sound('Bonk.wav')
FONT_SIZE = 100

class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.center = (400, 300)
        self.frame_index = 0
        self.animation_frames = [self.image, pygame.transform.flip(self.image, True, False)]

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 20
        if keys[pygame.K_RIGHT]:
            self.rect.x += 20
        if keys[pygame.K_UP]:
            self.rect.y -= 20
        if keys[pygame.K_DOWN]:
            self.rect.y += 20

        self.frame_index += 0.4
        if self.frame_index >= len(self.animation_frames):
            self.frame_index = 0
        self.image = self.animation_frames[int(self.frame_index)]
        

class Enimy(pygame.sprite.Sprite):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, 800), random.randint(0, 600))

    def update(self):
        self.rect.y += 5
        if self.rect.top > 600:
            self.rect.bottom = 0
            self.rect.x = random.randint(250, 800)

class End(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect() 
        self.rect.topleft = (x, y)
        
def stolk():
    if pygame.sprite.spritecollide(sprite, enimys, False):
        global game_time
        game_time = game_time - 1
        sound_effect.play()
        print('Столкновение!')

def the_end():
    if pygame.sprite.spritecollide(sprite, doors, False):
        global running
        running = False
        draw_text("Победа", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20, (0, 0, 0))
        pygame.display.flip()
        
def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

font = pygame.font.Font(None, FONT_SIZE)
game_time = 20
enimys = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
doors = pygame.sprite.Group()
sprite = MySprite('костюм 1.svg', 20, 500)
enimy = Enimy('crab-a.svg')
enimy2 = Enimy('crab-a.svg')
enimy3 = Enimy('crab-a.svg')
enimy4 = Enimy('crab-a.svg')
enimy5 = Enimy('crab-a.svg')
apple = End('Apple.svg', 700, 10)
doors.add(apple)
enimys.add(enimy, enimy2, enimy3, enimy4, enimy5)
all_sprites.add(sprite)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    elapsed_time =  pygame.time.get_ticks() // 1000
    remaining_time = max(0, game_time - elapsed_time)
    if elapsed_time > game_time:
         running = False
    
    screen.fill(black)
    stolk()
    the_end()
    image = pygame.image.load('фон.jpg')
    resized_image = pygame.transform.scale(image, (800, 800))
    screen.blit(resized_image, (0, 0))
    all_sprites.draw(screen)
    enimys.draw(screen)
    doors.draw(screen)
    enimys.update()
    all_sprites.update()
    draw_text(f"Time: {remaining_time}", SCREEN_WIDTH - 770, 10, (0, 0, 0))
    pygame.display.flip()
    clock.tick(60)
if elapsed_time > game_time:
    draw_text("Game Over", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20, (0, 0, 0))
pygame.display.flip()
the_end()
pygame.time.wait(3000)
    
pygame.quit()
    
