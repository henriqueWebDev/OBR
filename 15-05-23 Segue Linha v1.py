#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

#ev3
ev3 = EV3Brick()

#inicando motores
motorEsquerdo = Motor(Port.A, gears=[24, 24, 24 , 24, 24])
motorDireito = Motor(Port.B, gears=[24, 24, 24 , 24, 24])

#inicia DriveBase
robo = DriveBase(motorEsquerdo, motorDireito, wheel_diameter=55, axle_track=200)

#iniciando sensores de cor
sensorCorEsquerda = ColorSensor(Port.S1)
sensorCorDireita = ColorSensor(Port.S2)

#iniciando sensor ultrasonico
ultraSonico = UltrasonicSensor(Port.S3)

# Obstaculo
def volta_obstaculo():

    # ajusta o robo se quando ele detectar o obstaculo e tiver na linha preta
    if sensorCorEsquerda.color() == Color.BLACK:
        while sensorCorEsquerda.color() != Color.WHITE:
            robo.drive(0,-25)
    elif sensorCorDireita.color() == Color.BLACK:
        while sensorCorDireita.color() != Color.WHITE:
            robo.drive(0,25)

    # realiza o desvio
    robo.turn(90)
    robo.straight(140)
    robo.turn(-45)
    robo.straight(140)
    robo.turn(-45)
    robo.straight(260)
    robo.turn(-45)
    robo.straight(140)
    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(50,-18)
    while sensorCorDireita.color() != Color.WHITE:
        robo.drive(50,0)
    robo.straight(10)
    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(0,50)
    ev3.speaker.beep()

while True:

    robo.drive(90,0)

    if (sensorCorEsquerda.reflection() > 99 and sensorCorDireita.reflection() > 99):
        ev3.speaker.beep()

    # obstaculo
    if ultraSonico.distance() < 50:
        volta_obstaculo()

    # <teste verde>
    if sensorCorEsquerda.color() == Color.GREEN:
        while sensorCorEsquerda.color() != Color.BLACK:
            robo.drive(0,50)
        robo.turn(-10)
        if sensorCorEsquerda.color() == Color.GREEN:# confirma o verde
            while sensorCorEsquerda.color() != Color.WHITE:
                robo.drive(-30,0)
            robo.drive(30,0)
            # teste de verde e dois verdes
            while sensorCorEsquerda.color() != Color.BLACK or sensorCorDireita.color() != Color.GREEN:
                if sensorCorEsquerda.color() == Color.BLACK:
                    robo.turn(-10)
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(50,0)
                    robo.turn(-25)
                    while sensorCorEsquerda.color() != Color.WHITE:
                        robo.drive(50,0)
                    robo.straight(50)
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(0,-50)
                    break
                elif sensorCorDireita.color() == Color.GREEN:# dois verdes
                    robo.straight(-20)
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(0,50)
            
    elif sensorCorDireita.color() == Color.GREEN:
        while sensorCorDireita.color() != Color.BLACK:
            robo.drive(0,-50)
        robo.turn(10)
        if sensorCorDireita.color() == Color.GREEN:# confirma o verde
            while sensorCorDireita.color() != Color.WHITE:
                robo.drive(-30,0)
            robo.drive(30,0)
            # teste de verde e dois verdes
            while sensorCorDireita.color() != Color.BLACK or sensorCorEsquerda.color() != Color.GREEN:
                if sensorCorDireita.color() == Color.BLACK:
                    robo.turn(10)
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(50,0)
                    robo.turn(25)
                    while sensorCorDireita.color() != Color.WHITE:
                        robo.drive(50,0)
                    robo.straight(50)
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(0,50)
                    break
                elif sensorCorEsquerda.color() == Color.GREEN:# dois verdes
                    robo.straight(-20)
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(0,-50)
    # </teste verde>

    # <teste preto>
    if sensorCorEsquerda.color() == Color.BLACK:
        while sensorCorEsquerda.color() != Color.WHITE:
            if sensorCorDireita.color() == Color.BLACK:
                # <dois pretos>
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(0,25)
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(90,0)
                robo.turn(10)
                robo.straight(40)
                if sensorCorEsquerda.color() != Color.BLACK:
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(0,-50)
                        if sensorCorDireita.color() == Color.BLACK:
                            break
                # </dois pretos>
            robo.drive(0, -25)

    elif sensorCorDireita.color() == Color.BLACK:
        while sensorCorDireita.color() != Color.WHITE:
            if sensorCorEsquerda.color() == Color.BLACK:
                # <dois pretos>
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(0,-25)
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(90,0)
                robo.turn(10)
                robo.straight(40)
                if sensorCorDireita.color() != Color.BLACK:
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(0,50)
                        if sensorCorEsquerda.color() == Color.BLACK:
                            break
                # </dois pretos>
            robo.drive(0, 25)
    # </teste preto>