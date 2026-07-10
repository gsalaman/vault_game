# this version JUST drives the key leds/buttons.  Gonna start here to make sure my python logic is good.
key_circle = neopixel.create(DigitalPin.P2, 16, NeoPixelMode.RGB)
key_state = "wait_for_press"
key_count = 0
key_next_update_ms = 0
rgb_green = 0x00ff00
rgb_red = 0xff0000
rgb_blue = 0x0000ff
rgb_yellow = 0xffff00
rgb_black = 0x00

def key_process_wait_for_press():
    global key_state, key_circle
    if (pins.digital_read_pin(DigitalPin.P11) == 0):
        key_state = "spin"
        key_circle.show_color(rgb_black)
        key_circle.set_pixel_color(0, rgb_green)
        key_circle.show()

def key_process_spin():
    global key_next_update_ms, key_circle, key_count, key_state
    # is it time to do an update?
    time_now_ms = input.running_time()
    if (time_now_ms > key_next_update_ms):
        #advance the LED
        key_circle.rotate(-1)
        key_circle.show()
        # calculate the next update input_running_time
        key_next_update_ms = time_now_ms + 50
        key_count = key_count + 1
    
    # we're gonna count how many times we've done a "spin"
    # if we do 3 rotations (48), we're done...move on to flashing
    if (key_count > 48):
        key_count = 0
        key_state = "flash"


def key_process_flash():
    global key_count, key_next_update_ms, key_circle, key_state
    # is it time to do an update?
    time_now_ms = input.running_time()
    if (time_now_ms > key_next_update_ms):
        # 3 ons, 3 offs makes 6 iterations through this state
        if (key_count < 6):
            # odds are on, evens are offs
            if (key_count % 2 == 0):
                key_circle.show_color(rgb_green)
            else:
                key_circle.show_color(rgb_black)
            key_count = key_count + 1

            # 200 ms between flashes
            key_next_update_ms = time_now_ms + 200
        else:
            key_circle.show_color(rgb_black)
            key_state = "wait_for_press"

def drive_key_state():
    if (key_state == "wait_for_press"):
        key_process_wait_for_press()
    elif (key_state == "spin"):
        key_process_spin()
    elif (key_state == "flash"):
        key_process_flash()

def on_forever():
    drive_key_state()
    


basic.forever(on_forever)
