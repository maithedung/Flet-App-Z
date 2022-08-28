import webbrowser

from flet import (
    Column,
    Container,
    Text,
    UserControl,
    padding,
    alignment,
    CircleAvatar,
    colors,
    Divider,
    border_radius,
    ListTile,
    Icon, icons, Image
)


class MeCardAppControl(UserControl):
    # link of your profiles
    def __init__(self):
        super().__init__()
        self.info = {
            'phone': '+84 9325 02578',
            'email': 'maithedungg@gmail.com',
            'twitter': '@maithedungg',
            'github': '@maithedung'
        }
        self.urls = [
            "tel://+84932502578",
            "mailto://maithedungg@gmail.com",
            "https://twitter.com/maithedungg",
            "https://github.com/maithedung"
        ]
        self.avatar = CircleAvatar(
            background_image_url="/images/avatar.png",
            bgcolor=colors.WHITE,
            max_radius=100
        )
        self.name = Text(
            value='Mai The Dung',
            size=40,
            font_family='Kanit'
        )
        self.position = Text(
            value='Backend Developer',
            size=30,
            color=colors.WHITE30
        )
        self.divider = Divider(
            color=colors.WHITE,
            thickness=2,
            height=50
        )
        self.container = Container(
            width=1000,
            padding=padding.symmetric(
                horizontal=20,
                vertical=10
            ),
            content=self.divider
        )

        # Phone
        self.call_icon = Icon(
            name=icons.CALL,
            color=colors.BLACK,
            size=50
        )
        self.call_tile = self.tile_widget(
            icon=self.call_icon,
            title=self.info['phone'],
            index=0
        )

        # Email
        self.email_icon = Icon(
            name=icons.EMAIL,
            color=colors.BLACK,
            size=50
        )
        self.email_tile = self.tile_widget(
            icon=self.email_icon,
            title=self.info['email'],
            index=1
        )

        # Twitter
        self.twitter_image = Image(
            src="/images/twitter.png",
            fit="contain"
        )

        self.twitter_tile = self.tile_widget(
            icon=self.twitter_image,
            title=self.info['twitter'],
            index=2
        )

        # Github
        self.github_image = Image(
            src="/images/github.png",
            fit="contain"
        )

        self.github_tile = self.tile_widget(
            icon=self.github_image,
            title=self.info['github'],
            index=3
        )

        self.body = Column(
            alignment='center',
            horizontal_alignment='center',
            # fixed vertical spacing in b/w child controls
            spacing=20,
            controls=[
                self.avatar,
                self.name,
                self.position,
                self.container,
                self.call_tile,
                self.email_tile,
                self.twitter_tile,
                self.github_tile
            ]
        )

    def tile_widget(self, icon, title, index):
        title = Text(
            value=title,
            color=colors.BLACK
        )
        list_tile = ListTile(
            leading=icon,
            title=title,
            on_click=lambda _: self.on_click(index=index)
        )
        tile = Container(
            width=1000,
            padding=padding.symmetric(horizontal=20, vertical=10),
            bgcolor=colors.WHITE,
            alignment=alignment.center,
            border_radius=border_radius.all(8),
            content=list_tile
        )
        return tile

    def on_click(self, index):
        webbrowser.open_new_tab(self.urls[index])

    def build(self):
        view = Container(
            # using padding control
            padding=padding.symmetric(
                horizontal=20,
                vertical=50
            ),
            # alignment for aligning content in center
            alignment=alignment.center,
            content=self.body
        )

        return view
