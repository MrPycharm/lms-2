import pygame
from pygame.locals import *


def main():
    pygame.init()

    WIDTH, HEIGHT = 800, 600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Игровое поле")

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    player1_pos = [100, 100]
    player2_pos = [600, 100]
    player_size = 50

    player1_controls = {"up": K_w, "down": K_s, "left": K_a, "right": K_d}
    player2_controls = {"up": K_UP, "down": K_DOWN, "left": K_LEFT, "right": K_RIGHT}
    player_speed = 20
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        clock.tick(60)
        screen.fill(BLACK)

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    player1_pos[0] -= 1
                if e.key == pygame.K_RIGHT:
                    player1_pos[0] += 1
                if e.key == pygame.K_UP:
                    player1_pos[1] -= 1
                if e.key == pygame.K_DOWN:
                    player1_pos[1] += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1_pos[0] -= 1
        if keys[pygame.K_RIGHT]:
            player1_pos[0] += 1
        if keys[pygame.K_UP]:
            player1_pos[1] -= 1
        if keys[pygame.K_DOWN]:
            player1_pos[1] += 1

        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    player2_pos[0] -= 1
                if e.key == pygame.K_d:
                    player2_pos[0] += 1
                if e.key == pygame.K_w:
                    player2_pos[1] -= 1
                if e.key == pygame.K_s:
                    player2_pos[1] += 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player2_pos[0] -= 1
        if keys[pygame.K_d]:
            player2_pos[0] += 1
        if keys[pygame.K_w]:
            player2_pos[1] -= 1
        if keys[pygame.K_s]:
            player2_pos[1] += 1

        # Очистка экрана

        # Отрисовка игрового поля
        pygame.draw.rect(screen, WHITE, (50, 50, WIDTH - 100, HEIGHT - 100), 2)

        # Отрисовка персонажей
        pygame.draw.rect(screen, WHITE, (player1_pos[0], player1_pos[1], player_size, player_size))
        pygame.draw.rect(screen, WHITE, (player2_pos[0], player2_pos[1], player_size, player_size))

        # Обновление экрана
        pygame.display.flip()

        # Ограничение количества кадров в секунду
        clock.tick(60)

if __name__ == '__main__':
    main()