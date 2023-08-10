colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
]


def cool_light_show():
    led = led_ctrl
    delay = 0.2  # Delay between light transitions

    # Iterate through each color
    for color in colors:
        r, g, b = color

        # Set all top LEDs to the current color
        led.set_top_led(rm_define.armor_top_all, r, g, b, rm_define.effect_always_on)

        # Flash bottom LEDs with the current color
        led.set_bottom_led(rm_define.armor_bottom_all, r, g, b, rm_define.effect_flash)

        time.sleep(delay)

        # Turn off the bottom LEDs
        led.set_bottom_led(rm_define.armor_bottom_all, 0, 0, 0, rm_define.effect_always_off)

        time.sleep(delay)

    # Turn off all LEDs
    led.turn_off(rm_define.armor_all)


# Start the cool light show
cool_light_show()
