distance = 0
strip = False

def on_forever():
    global distance, strip
    distance = maqueen.ultrasonic(PingUnit.CENTIMETERS)
    if distance < 20 and distance != 0:
        strip = Math.random_boolean()
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 0)
        basic.pause(1000)
        if strip == True:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 200)
            basic.pause(800)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 0)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
            basic.pause(800)
        else:
            maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CCW, 200)
            basic.pause(800)
            maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
            maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 0)
            basic.pause(800)
    else:
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 50)
        basic.pause(1000)
basic.forever(on_forever)
