// Switch mode
input.onButtonPressed(Button.A, function () {
    master = !(master)
})
// Radio trigger on master
radio.onReceivedValue(function (name, value) {
    if (master) {
        if (name == "temp") {
            temperature = value
        } else if (name == "light") {
            light_level = value
        }
        light_angle = Math.floor(Math.map(light_level, 0, 255, 0, 180))
        temperature_angle = Math.floor(Math.map(temperature, -5, 50, 0, 180))
        serial.writeNumbers([light_angle, temperature_angle])
        servos.P0.setAngle(temperature_angle)
        servos.P1.setAngle(light_angle)
    }
    basic.pause(1000)
})
let temperature_angle = 0
let light_angle = 0
let light_level = 0
let temperature = 0
let master = false
serial.redirectToUSB()
master = false
radio.setGroup(42)
temperature = 0
light_level = 0
// remote measure loop
basic.forever(function () {
    if (!(master)) {
        servos.P0.setAngle(0)
        servos.P1.setAngle(0)
        temperature = input.temperature()
        light_level = input.lightLevel()
        radio.sendValue("temp", temperature)
        radio.sendValue("light", light_level)
        basic.pause(2000)
    }
    basic.pause(1000)
})
// Master display loop
basic.forever(function () {
    if (master) {
        whaleysans.showNumber(Math.abs(temperature))
        basic.pause(2000)
        whaleysans.showNumber(Math.floor(Math.map(light_level, 0, 255, 0, 99)))
    }
    basic.pause(2000)
})
