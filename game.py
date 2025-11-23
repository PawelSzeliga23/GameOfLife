import pygame
import numpy as np

col_alive = (255, 255, 255)
col_background = (0, 0, 0)
col_grid = (15, 15, 15)


def draw_text(surface, text, x, y, size, colour=(255, 255, 255)):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, colour)
    surface.blit(text, (x, y))


def draw_textfield(surface, rect, text, active):
    color = (0, 100, 255) if active else (45, 45, 45)
    pygame.draw.rect(surface, color, rect, 0)
    pygame.draw.rect(surface, (255, 255, 255), rect, 2)

    font = pygame.font.Font(None, 20)
    text_surface = font.render(text, True, (255, 255, 255))
    surface.blit(text_surface, (rect.x + 5, rect.y + 5))


def update(surface, cur, cell_size, rules):
    next = np.zeros((cur.shape[0], cur.shape[1]))

    for i, j in np.ndindex(cur.shape):
        top = cur[i - 1, j]
        bottom = cur[(i + 1) % cur.shape[0], j]
        left = cur[i, j - 1]
        right = cur[i, (j + 1) % cur.shape[1]]
        top_left = cur[i - 1, j - 1]
        top_right = cur[i - 1, (j + 1) % cur.shape[1]]
        bottom_left = cur[(i + 1) % cur.shape[0], j - 1]
        bottom_right = cur[(i + 1) % cur.shape[0], (j + 1) % cur.shape[1]]
        num_alive = int(top + bottom + left + right + top_left + top_right + bottom_left + bottom_right)

        current = int(cur[i, j])
        next[i, j] = rules[current, num_alive]

        col = col_alive if cur[i, j] == 1 else col_background
        pygame.draw.rect(surface, col, (j * cell_size, i * cell_size, cell_size - 1, cell_size - 1))

    return next


def print_cells(cells, surface, cell_size):
    dim_y, dim_x = cells.shape
    for y in range(dim_y):
        for x in range(dim_x):
            if cells[y, x] == 1:
                pygame.draw.rect(surface, col_alive, (x * cell_size, y * cell_size, cell_size - 1, cell_size - 1))
            else:
                pygame.draw.rect(surface, col_background, (x * cell_size, y * cell_size, cell_size - 1, cell_size - 1))


def init(dim_x, dim_y):
    cells = np.zeros((dim_y, dim_x))
    return cells


def make_rules(rules):
    rules = rules.split("/")
    result = np.zeros((2, 9))
    for r in rules[0]:
        result[1, int(r)] = 1
    for r in rules[1]:
        result[0, int(r)] = 1
    return result


def main(dim_x, dim_y, cell_size):
    pygame.init()
    surface = pygame.display.set_mode((dim_x * cell_size, dim_y * cell_size))
    pygame.display.set_caption("Game of Life")
    rect = pygame.Rect(65, 70, 60, 20)
    active = False
    text = "23/3"
    rules = make_rules("23/3")
    cells = init(dim_x, dim_y)
    begin_cells = None
    is_on = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not is_on:
                    if rect.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                        x, y = pygame.mouse.get_pos()
                        x //= cell_size
                        y //= cell_size
                        cells[y, x] = 1 - cells[y, x]
                        begin_cells = np.copy(cells)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_on:
                        is_on = False
                    else:
                        is_on = True
                elif event.key == pygame.K_c:
                    cells = init(dim_x, dim_y)
                elif event.key == pygame.K_r:
                    cells = begin_cells.copy()
                elif active:
                    if event.key == pygame.K_RETURN:
                        try:
                            rules = make_rules(text)
                        except:  # noqa
                            rules = make_rules("23/3")
                            text = "23/3"
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        surface.fill(col_grid)
        if not is_on:
            print_cells(cells, surface, cell_size)
        if is_on:
            cells = update(surface, cells, cell_size, rules)
        if is_on:
            colour = (0, 255, 0)
        else:
            colour = (255, 0, 0)
        draw_text(surface, "ON" if is_on else "OFF", 10, 10, 20, colour)
        draw_text(surface, "C - CLEAR", 10, 30, 20)
        draw_text(surface, "R - RESET", 10, 50, 20)
        draw_text(surface, "RULES:", 10, 73, 20)
        draw_textfield(surface, rect, text, active)
        pygame.display.update()


if __name__ == "__main__":
    main(120, 80, 10)
