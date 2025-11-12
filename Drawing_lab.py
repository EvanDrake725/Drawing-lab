import pygame, math

def image(background):
    #draw a hat
    pygame.draw.ellipse(background, (0, 0, 0), ((150, 145), (320, 50)),0)
    pygame.draw.rect(background, (0, 0, 0), ((255, 45), (112, 105)), 55)

    #draw the head
    pygame.draw.ellipse(background, (0, 180, 0), ((150, 170), (320, 150)), 0)

    #draw the eyes
    pygame.draw.circle(background, (0, 150, 0), (406, 180), 50)
    pygame.draw.circle(background, (225, 225, 225), (406, 180), 45)
    pygame.draw.circle(background, (0, 0, 0), (406, 180), 10)
    pygame.draw.arc(background, (0, 150, 0), ((359, 125), (100, 100)), 0, math.pi/1, 100)
    
    pygame.draw.circle(background, (0, 150, 0), (210, 180), 50)
    pygame.draw.circle(background, (225, 225, 225), (210, 180), 45)
    pygame.draw.circle(background, (0, 0, 0), (210, 180), 10)
    pygame.draw.arc(background, (0, 150, 0), ((162, 125), (100, 100)), 0, math.pi/1, 100)
    
    #draw the mouth
    pygame.draw.arc(background, (0, 0, 0), ((210, 219), (200, 50)), 2.75, math.pi/12, 7)

    #draw the tounge
    pygame.draw.rect(background, (231, 84, 128), ((262, 258), (92, 92)), 50)
    pygame.draw.circle(background, (231, 84, 128), (308, 347), 48)
    pygame.draw.line(background, (255, 182, 193), (304, 264), (304, 384))




def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("My little Chudling")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((200, 200, 255))
    image(background)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        screen.blit(background, (0, 0))
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()