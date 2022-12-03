
import arcade

def test_stuff():
    arcade.open_window(600, 600, "Drawing Example")

    arcade.set_background_color(arcade.csscolor.LIGHT_STEEL_BLUE)

    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.ALICE_BLUE)
    arcade.finish_render()

    arcade.run()