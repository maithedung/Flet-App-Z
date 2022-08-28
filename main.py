import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors

from calculator_app.calc import CalculatorAppControl
from mecard_app.me_card import MeCardAppControl
from todo_app.todo import TodoAppControl


def main(page: Page):
    home_title = 'Flet App Z'
    home_url = '/'
    todo_title = 'Todo App'
    todo_url = '/todo_app'
    calculator_title = 'Calculator App'
    calculator_url = '/calculator_app'
    mecard_title = 'MeCard App'
    mecard_url = '/mecard_app'

    page.title = home_title
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }

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
    elevated_button_mecard = ElevatedButton(
        text=mecard_title,
        on_click=lambda _: page.go(mecard_url)
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
            elevated_button_calc,
            elevated_button_mecard
        ],
        scroll='adaptive'
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
        horizontal_alignment='center',
        scroll='adaptive'
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

    # MeCard App Page
    text4 = Text(
        value=mecard_title
    )
    app_bar4 = AppBar(
        title=text4,
        bgcolor=colors.SURFACE_VARIANT
    )
    me_card = MeCardAppControl()
    view4 = View(
        route=home_url,
        controls=[
            app_bar4,
            me_card
        ],
        horizontal_alignment='center',
        scroll='adaptive'
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
        if page.route == mecard_url:
            page.views.append(
                view4
            )


        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


flet.app(
    target=main,
    route_url_strategy="path",
    assets_dir="assets",
    view=flet.WEB_BROWSER
)
