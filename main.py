import sys
import pygame

# Define las constantes
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 170
X_AXIS = 0
Y_AXIS = 1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define la clase Lines para dibujar la cuadricula


class Lines:
    def __init__(self, axis, line_n):
        self.length = TILE_SIZE * 3 + 2
        if axis == X_AXIS:
            pos_x = (WIDTH - self.length) // 2
            pos_y = (HEIGHT - self.length) // 2 + TILE_SIZE * line_n + 1 * line_n - 2
            self.pos = (pos_x, pos_y)
            self.surf = pygame.Surface((self.length, 5))
            self.surf.fill(BLACK)
            self.rect = self.surf.get_rect()
        elif axis == Y_AXIS:
            pos_x = (WIDTH - self.length) // 2 + TILE_SIZE * line_n + 1 * line_n - 2
            pos_y = ((HEIGHT - self.length) // 2)
            self.pos = (pos_x, pos_y)
            self.surf = pygame.Surface((5, self.length))
            self.surf.fill(BLACK)
            self.rect = self.surf.get_rect()

# Define la clase Tiles para crear las zonas clicables


class Tile:
    def __init__(self, row, column):
        self.length = TILE_SIZE * 3 + 2
        self.row = row
        self.column = column
        pos_x = (WIDTH - self.length) // 2 + column * TILE_SIZE + 1 * column
        pos_y = (HEIGHT - self.length) // 2 + row * TILE_SIZE + 1 * row
        self.pos = (pos_x, pos_y)
        # Revisar 3 lineas inferiores
        self.surf = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(topleft=self.pos)


class Sprite:
    def __init__(self, row, column, shape):
        self.length = TILE_SIZE * 3 + 2
        pos_x = (WIDTH - self.length) // 2 + column * TILE_SIZE + 1 * column - TILE_SIZE // 2
        pos_y = (HEIGHT - self.length) // 2 + row * TILE_SIZE + 1 * row - TILE_SIZE // 2
        self.pos = (pos_x, pos_y)
        if shape == "x":
            self.image = pygame.image.load("images/x_shape.png")
            self.rect = self.image.get_rect(center=(500, 500))
        elif shape == "o":
            self.image = pygame.image.load("images/circle.png")
            self.rect = self.image.get_rect(center=(500, 500))


# Inicializa la ventana de juego

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
window.fill(WHITE)

# Define las listas de objetos tiles y lines
tiles = [Tile(0, 0), Tile(0, 1), Tile(0, 2), Tile(1, 0), Tile(1, 1), Tile(1, 2), Tile(2, 0), Tile(2, 1), Tile(2, 2)]
lines = [Lines(X_AXIS, 1), Lines(X_AXIS, 2), Lines(Y_AXIS, 1), Lines(Y_AXIS, 2)]

# Dibuja la cuadricula y las zonas clicables
for i in range(0, 9):
    window.blit(tiles[i].surf, tiles[i].rect)
for i in range(0, 4):
    window.blit(lines[i].surf, lines[i].pos)

sprites = []

# Main loop del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for i in range(0, 9):
                if tiles[i].rect.collidepoint(mouse_pos):
                    sprites.append(Sprite(tiles[i].row, tiles[i].column, "x"))
                    # Error en la linea anterior lo demas funciona
    pygame.display.update()
