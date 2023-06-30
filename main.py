import pygame

class Game: #initialization screen
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.running = True

        while self.running: #standby screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

if __name__=="__main__":
    game = Game()