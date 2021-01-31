Light_State = 0

def on_pin_pressed_p0():
    global Light_State
    if Light_State == 0:
        Light_State = 1
    else:
        Light_State = 0
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_forever():
    if Light_State == 1:
        while Light_State == 1:
            pins.analog_write_pin(AnalogPin.P2, pins.analog_read_pin(AnalogPin.P1))
            basic.pause(pins.analog_read_pin(AnalogPin.P1))
            pins.digital_write_pin(DigitalPin.P2, 0)
            basic.pause(100)
    else:
        pins.digital_write_pin(DigitalPin.P2, 0)
basic.forever(on_forever)
