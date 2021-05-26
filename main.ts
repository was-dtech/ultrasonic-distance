let distance = 0
let strip = false
basic.forever(function () {
    distance = maqueen.Ultrasonic(PingUnit.Centimeters)
    if (distance < 20 && distance != 0) {
        strip = Math.randomBoolean()
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 0)
        basic.pause(1000)
    } else {
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 50)
        basic.pause(1000)
        if (strip == true) {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 200)
            basic.pause(800)
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
            basic.pause(800)
        } else {
            maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CCW, 200)
            basic.pause(800)
            maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            basic.pause(800)
        }
    }
})
