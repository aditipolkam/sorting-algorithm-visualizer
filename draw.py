from draw_list import draw_list
import pygame


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(
        f"{algo_name} - {'Ascending' if ascending else 'Descending'}",
        1,
        draw_info.BLACK,
    )
    draw_info.window.blit(title, (draw_info.width / 2 - title.get_width() / 2, 0))

    controls = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending",
        1,
        draw_info.BLACK,
    )
    draw_info.window.blit(
        controls, (draw_info.width / 2 - controls.get_width() / 2, 45)
    )

    sorting = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK
    )
    draw_info.window.blit(sorting, (draw_info.width / 2 - sorting.get_width() / 2, 75))

    draw_list(draw_info)
    pygame.display.update()
