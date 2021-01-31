let Light_State = 0
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    
    if (Light_State == 0) {
        Light_State = 1
    } else {
        Light_State = 0
    }
    
})
basic.forever(function on_forever() {
    if (Light_State == 1) {
        while (Light_State == 1) {
            pins.analogWritePin(AnalogPin.P2, pins.analogReadPin(AnalogPin.P1))
            basic.pause(pins.analogReadPin(AnalogPin.P1))
            pins.digitalWritePin(DigitalPin.P2, 0)
            basic.pause(100)
        }
    } else {
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    
})
