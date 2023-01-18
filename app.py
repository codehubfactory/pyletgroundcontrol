import flet as ft
import pymavlink
import dronekit
import ui.widget.altitude_horizontal.altitude_horizontal as altitude_horizontal
# import ui.widget.appbar.appbar_control as appbar_control
import ui.widget.appbar.appbar_control as appbar_control

def main(page: ft.Page):
    
    
    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        # page.update()

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.CONTROL_POINT,color=ft.colors.RED),
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
                        text="Checked item", checked=False, on_click=check_item_clicked
                    ),
                ]
            ),
        ],
    )
    
    # page.appbar=appbar_control.AppBar_Control().getcustomappbar()
    # print(altitude_horizontal.Display().control2base64())
    page.add(ft.Container(
        ft.Image(src_base64=altitude_horizontal.Display().control2base64().decode("utf-8"))
    ))
    page.add(ft.Text("Body!"))

ft.app(target=main)