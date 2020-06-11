def on_button_pressed_a():
    global master
    master = not (master)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_value(name, value):
    global temperature, light_level, light_angle, temperature_angle
    if master:
        if name == "temp":
            temperature = value
        elif name == "light":
            light_level = value
        light_angle = Math.floor(Math.map(light_level, 0, 255, 0, 180))
        temperature_angle = Math.floor(Math.map(temperature, -5, 50, 0, 180))
        serial.write_numbers([light_angle, temperature_angle])
        servos.P0.set_angle(temperature_angle)
        servos.P1.set_angle(light_angle)
    basic.pause(1000)
radio.on_received_value(on_received_value)

temperature_angle = 0
light_angle = 0
light_level = 0
temperature = 0
master = False
serial.redirect_to_usb()
master = False
radio.set_group(42)
temperature = 0
light_level = 0

def on_forever():
    global temperature, light_level
    if not (master):
        servos.P0.set_angle(0)
        servos.P1.set_angle(0)
        temperature = input.temperature()
        light_level = input.light_level()
        radio.send_value("temp", temperature)
        radio.send_value("light", light_level)
        basic.pause(2000)
    basic.pause(1000)
basic.forever(on_forever)

def on_forever2():
    if master:
        whaleysans.show_number(abs(temperature))
        basic.pause(2000)
        whaleysans.show_number(Math.floor(Math.map(light_level, 0, 255, 0, 99)))
    basic.pause(2000)
basic.forever(on_forever2)
