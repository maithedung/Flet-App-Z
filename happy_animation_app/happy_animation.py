import random
from math import pi

from flet import Container, ElevatedButton, Stack, colors, UserControl


class HappyAnimationControl(UserControl):
    def __init__(self):
        super().__init__()
        self.size = 40
        self.gap = 6
        self.duration = 2000

        self.c1 = colors.PINK_500
        self.c2 = colors.AMBER_500
        self.c3 = colors.LIGHT_GREEN_500
        self.c4 = colors.DEEP_PURPLE_500

        self.all_colors = [
            colors.AMBER_400,
            colors.AMBER_ACCENT_400,
            colors.BLUE_400,
            colors.BROWN_400,
            colors.CYAN_700,
            colors.DEEP_ORANGE_500,
            colors.CYAN_500,
            colors.INDIGO_600,
            colors.ORANGE_ACCENT_100,
            colors.PINK,
            colors.RED_600,
            colors.GREEN_400,
            colors.GREEN_ACCENT_200,
            colors.TEAL_ACCENT_200,
            colors.LIGHT_BLUE_500,
        ]

        self.parts = [
            # F
            (0, 0, self.c1),
            (0, 1, self.c1),
            (0, 2, self.c1),
            (0, 3, self.c1),
            (0, 4, self.c1),
            (1, 0, self.c1),
            (1, 2, self.c1),
            (2, 0, self.c1),
            # L
            (4, 0, self.c2),
            (4, 1, self.c2),
            (4, 2, self.c2),
            (4, 3, self.c2),
            (4, 4, self.c2),
            (5, 4, self.c2),
            (6, 4, self.c2),
            # E
            (8, 0, self.c3),
            (9, 0, self.c3),
            (10, 0, self.c3),
            (8, 1, self.c3),
            (8, 2, self.c3),
            (9, 2, self.c3),
            (10, 2, self.c3),
            (8, 3, self.c3),
            (8, 4, self.c3),
            (9, 4, self.c3),
            (10, 4, self.c3),
            # T
            (12, 0, self.c4),
            (13, 0, self.c4),
            (14, 0, self.c4),
            (13, 1, self.c4),
            (13, 2, self.c4),
            (13, 3, self.c4),
            (13, 4, self.c4),
        ]

        self.width = 16 * (self.size + self.gap)
        self.height = 5 * (self.size + self.gap)

        self.canvas = Stack(
            width=self.width,
            height=self.height,
            animate_scale=self.duration,
            animate_opacity=self.duration,
        )

        self.go_button = ElevatedButton("Go!", on_click=self.assemble)
        self.again_button = ElevatedButton("Again!", on_click=self.randomize)

        # spread parts randomly
        for i in range(len(self.parts)):
            self.canvas.controls.append(
                Container(
                    animate=self.duration,
                    animate_position=self.duration,
                    animate_rotation=self.duration,
                )
            )

    def randomize(self, e):
        random.seed()
        for i in range(len(self.parts)):
            c = self.canvas.controls[i]
            part_size = random.randrange(int(self.size / 2), int(self.size * 3))
            c.left = random.randrange(0, self.width)
            c.top = random.randrange(0, self.height)
            c.bgcolor = self.all_colors[random.randrange(0, len(self.all_colors))]
            c.width = part_size
            c.height = part_size
            c.border_radius = random.randrange(0, int(self.size / 2))
            c.rotate = random.randrange(0, 90) * 2 * pi / 360
        self.canvas.scale = 5
        self.canvas.opacity = 0.3
        self.go_button.visible = True
        self.again_button.visible = False
        self.update()

    def assemble(self, e):
        i = 0
        for left, top, bgcolor in self.parts:
            c = self.canvas.controls[i]
            c.left = left * (self.size + self.gap)
            c.top = top * (self.size + self.gap)
            c.bgcolor = bgcolor
            c.width = self.size
            c.height = self.size
            c.border_radius = 5
            c.rotate = 0
            i += 1
        self.canvas.scale = 1
        self.canvas.opacity = 1
        self.go_button.visible = False
        self.again_button.visible = True
        self.update()
        self.randomize(None)

        self.spacing = 30
        self.add(self.canvas, self.go_button, self.again_button)


