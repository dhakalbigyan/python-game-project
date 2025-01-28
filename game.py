import pygame
from sys import exit
pygame.init()

screen= pygame.display.set_mode((800,400))
pygame.display.set_caption('Bigyan Game')
clock = pygame.time.Clock()
test_font= pygame.font.Font(r'', 50)

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('Red')
sky_surface = pygame.image.load(r'').convert()
ground_surface = pygame.image.load(r'').convert()

score_surf = test_font.render('Bigyan Game','false','black')
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pygame.image.load(r'').convert_alpha()
snail_rect =snail_surface.get_rect(bottomright =(600,300))

player_surf = pygame.image.load(r'').convert_alpha()
player_rect = player_surf.get_rect(midbottom =(80,300))

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print("collid")

   screen.blit(sky_surface,(0,0))
   screen.blit(ground_surface, (0,300))  # Use `blit` instead of `blits`
   screen.blit(score_surf, score_rect)  # Use `blit` instead of `blits`
   pygame.draw.rect(screen,'pink', score_rect)
   pygame.draw.rect(screen,'pink', score_rect,6)

   snail_rect.x -=4
   if snail_rect.right <=0 : snail_rect.left =800
   screen.blit(snail_surface,snail_rect)
   player_rect.left +=1
   screen.blit(player_surf,player_rect)
   if player_rect.left >800 :player_rect.right =0


   player_rect.colliderect(snail_rect)

#    mouse_pos = pygame.mouse.get_pos()
#    if player_rect.collidepoint((mouse_pos)):
#        print('collision')
    
   pygame.display.update() 
   clock.tick(80)