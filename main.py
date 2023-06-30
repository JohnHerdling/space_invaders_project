import pygame

class Game: #initialization screen
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.background_img=pygame.image.load("spr_space_himmel.png")


        while self.running: #standby screen and game loob (alle permanet gezeigten Objekte)
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

if __name__=="__main__":
    game = Game(800, 600)