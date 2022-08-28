import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors

from calculator_app.calc import CalculatorAppControl
from todo_app.todo import TodoAppControl


def main(page: Page):
    home_title = 'Flet App Z'
    home_url = '/'
    todo_title = 'Todo App'
    todo_url = '/todo_app'
    calculator_title = 'Calculator App'
    calculator_url = '/calculator_app'

    page.title = home_title

    # Home Page
    text1 = Text(
        value=home_title
    )
    elevated_button_todo = ElevatedButton(
        text=todo_title,
        on_click=lambda _: page.go(todo_url)
    )
    elevated_button_calc = ElevatedButton(
        text=calculator_title,
        on_click=lambda _: page.go(calculator_url)
    )
    app_bar1 = AppBar(
        title=text1,
        bgcolor=colors.SURFACE_VARIANT
    )
    view1 = View(
        route=home_url,
        controls=[
            app_bar1,
            elevated_button_todo,
            elevated_button_calc
        ]
    )

    # Todo App Page
    text2 = Text(
        value=todo_title
    )
    elevated_button2 = ElevatedButton(
        text='Go Home',
        on_click=lambda _: page.go(home_url)
    )
    app_bar2 = AppBar(
        title=text2,
        bgcolor=colors.SURFACE_VARIANT
    )
    todo = TodoAppControl()
    view2 = View(
        route=home_url,
        controls=[
            app_bar2,
            todo
        ],
        horizontal_alignment='center'
    )

    # Calculator App Page
    text3 = Text(
        value=calculator_title
    )
    app_bar3 = AppBar(
        title=text3,
        bgcolor=colors.SURFACE_VARIANT
    )
    calc = CalculatorAppControl()
    view3 = View(
        route=home_url,
        controls=[
            app_bar3,
            calc
        ],
        horizontal_alignment='center',
        vertical_alignment='center'
    )

    def route_change(router):
        page.views.clear()
        page.views.append(
            view1
        )
        if page.route == todo_url:
            page.views.append(
                view2
            )
        if page.route == calculator_url:
            page.views.append(
                view3
            )

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(target=main, route_url_strategy="path", view=flet.WEB_BROWSER)
