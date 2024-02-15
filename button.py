import pygame

class Button:
    def __init__(self, x, y, width, height, color, text=''):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 15)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)