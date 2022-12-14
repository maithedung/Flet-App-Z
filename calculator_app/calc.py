from flet import ElevatedButton, Text, Row, UserControl, colors, Container, border_radius, Column


class CalculatorAppControl(UserControl):
    def __init__(self):
        super().__init__()
        self.operator = None
        self.operand1 = None
        self.new_operand = None
        self.result = Text(value="0", color=colors.WHITE, size=20)
        self.row_result = Row(
            alignment='end',
            controls=[
                self.result
            ]
        )
        self.row1 = Row(
            alignment='center',
            controls=[
                ElevatedButton(
                    text="AC",
                    bgcolor=colors.BLUE_GREY_100,
                    color=colors.BLACK,
                    expand=1,
                    on_click=self.button_clicked,
                    data="AC"
                ),
                ElevatedButton(
                    text="+/-",
                    bgcolor=colors.BLUE_GREY_100,
                    color=colors.BLACK,
                    expand=1,
                    on_click=self.button_clicked,
                    data="+/-"
                ),
                ElevatedButton(
                    text="%",
                    bgcolor=colors.BLUE_GREY_100,
                    color=colors.BLACK,
                    expand=1,
                    on_click=self.button_clicked,
                    data="%",
                ),
                ElevatedButton(
                    text="/",
                    bgcolor=colors.ORANGE,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="/",
                )
            ]
        )
        self.row2 = Row(
            alignment='center',
            controls=[
                ElevatedButton(
                    text="7",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="7",
                ),
                ElevatedButton(
                    text="8",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="8",
                ),
                ElevatedButton(
                    text="9",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="9",
                ),
                ElevatedButton(
                    text="*",
                    bgcolor=colors.ORANGE,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="*",
                ),
            ]
        )
        self.row3 = Row(
            alignment='center',
            controls=[
                ElevatedButton(
                    text="4",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="4",
                ),
                ElevatedButton(
                    text="5",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="5",
                ),
                ElevatedButton(
                    text="6",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="6",
                ),
                ElevatedButton(
                    text="-",
                    bgcolor=colors.ORANGE,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="-",
                ),
            ]
        )
        self.row4 = Row(
            alignment='center',
            controls=[
                ElevatedButton(
                    text="1",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="1",
                ),
                ElevatedButton(
                    text="2",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="2",
                ),
                ElevatedButton(
                    text="3",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="3",
                ),
                ElevatedButton(
                    text="+",
                    bgcolor=colors.ORANGE,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="+",
                ),
            ]
        )
        self.row5 = Row(
            alignment='center',
            controls=[
                ElevatedButton(
                    text="0",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=2,
                    on_click=self.button_clicked,
                    data="0",
                ),
                ElevatedButton(
                    text=".",
                    bgcolor=colors.WHITE24,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data=".",
                ),
                ElevatedButton(
                    text="=",
                    bgcolor=colors.ORANGE,
                    color=colors.WHITE,
                    expand=1,
                    on_click=self.button_clicked,
                    data="=",
                ),
            ]
        )
        self.body_view = Column(
            controls=[
                self.row_result,
                self.row1,
                self.row2,
                self.row3,
                self.row4,
                self.row5
            ]
        )

    def button_clicked(self, e):
        if self.result.value == "Error" or e.data == "AC":
            self.result.value = "0"
            self.reset()

        elif e.data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
            if self.result.value == "0" or self.new_operand is True:
                self.result.value = e.data
                self.new_operand = False
            else:
                self.result.value = self.result.value + e.data

        elif e.data in ("+", "-", "*", "/"):
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.operator = e.data
            if self.result.value == "Error":
                self.operand1 = "0"
            else:
                self.operand1 = float(self.result.value)
            self.new_operand = True

        elif e.data in "=":
            self.result.value = self.calculate(
                self.operand1, float(self.result.value), self.operator
            )
            self.reset()

        elif e.data in "%":
            self.result.value = float(self.result.value) / 100
            self.reset()

        elif e.data in "+/-":
            if float(self.result.value) > 0:
                self.result.value = "-" + str(self.result.value)

            elif float(self.result.value) < 0:
                self.result.value = str(
                    self.format_number(abs(float(self.result.value)))
                )

        self.update()

    def format_number(self, num):
        if num % 1 == 0:
            return int(num)
        else:
            return num

    def calculate(self, operand1, operand2, operator):

        if operator == "+":
            return self.format_number(operand1 + operand2)

        elif operator == "-":
            return self.format_number(operand1 - operand2)

        elif operator == "*":
            return self.format_number(operand1 * operand2)

        elif operator == "/":
            if operand2 == 0:
                return "Error"
            else:
                return self.format_number(operand1 / operand2)

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True

    def build(self):
        self.reset()

        view = Container(
            width=300,
            bgcolor=colors.BLACK,
            border_radius=border_radius.all(20),
            padding=20,
            content=self.body_view
        )

        return view
