import flet as ft
from typing import Optional

from flet.control import Control, OptionalNumber

def check_item_clicked(e):
    e.control.checked = not e.control.checked
    # page.update()
custom_AppBar=ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("PyletGroundControl V0.1"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        # text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )

class AppBar_Control:
    
    # def __init__(self) -> ft.AppBar:
    #     return custom_AppBar
    def __call__(self) -> ft.AppBar:
        return custom_AppBar
    @property
    def getcustomappbar(self):
        return ft.AppBar(
        leading=ft.Icon(ft.icons.PALETTE),
        leading_width=40,
        title=ft.Text("PyletGroundControl V0.1"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            ft.IconButton(ft.icons.FILTER_3),
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Item 1"),
                    ft.PopupMenuItem(),  # divider
                    ft.PopupMenuItem(
                        # text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
        
    