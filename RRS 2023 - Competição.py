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
def voltaObstaculo():

    # ajusta o robo se quando ele detectar o obstaculo e tiver na linha preta
    if sensorCorEsquerda.color() == Color.BLACK:
        while sensorCorEsquerda.color() != Color.WHITE:
            robo.drive(0,-25)
    elif sensorCorDireita.color() == Color.BLACK:
        while sensorCorDireita.color() != Color.WHITE:
            robo.drive(0,25)

    # realiza o desvio
    robo.turn(90)
    robo.straight(120)
    robo.turn(-45)
    robo.straight(140)
    robo.turn(-45)
    robo.straight(220)
    robo.turn(-45)
    robo.straight(80)
    robo.turn(-20)
    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(50,-18)
    robo.straight(30)
    while sensorCorDireita.color() != Color.BLACK:
        robo.drive(0,50) 
    while sensorCorDireita.color() != Color.WHITE:
        robo.drive(0,50) 

while True:
    
    if sensorCorEsquerda.color() == Color.BLACK:
        robo.stop()
        while sensorCorEsquerda.color() != Color.WHITE:
            robo.drive(0,-25)
            if sensorCorDireita.color() == Color.BLACK:
                robo.stop()
                robo.turn(30)
                robo.straight(60)
                while sensorCorEsquerda.color() != Color.BLACK:
                    robo.drive(0,-75)
            if sensorCorEsquerda.color() == Color.GREEN:
                robo.turn(-5)
                if sensorCorEsquerda.color() == Color.GREEN:
                    robo.turn(-5)
                    robo.stop()
                    break
                break
    elif sensorCorDireita.color() == Color.BLACK: 
        robo.stop()
        while sensorCorDireita.color() != Color.WHITE:
            robo.drive(0,25)
            if sensorCorEsquerda.color() == Color.BLACK:
                robo.stop()
                robo.turn(-30)
                robo.straight(60)
                while sensorCorDireita.color() != Color.BLACK:
                    robo.drive(0,75)
            if sensorCorDireita.color() == Color.GREEN:
                robo.turn(5)
                if sensorCorDireita.color() == Color.GREEN:
                    robo.turn(5)
                    robo.stop()
                    break
                break

    if sensorCorEsquerda.color() == Color.GREEN:
        robo.straight(5)
        robo.stop() 
        robo.turn(-10)
        if sensorCorEsquerda.color() == Color.BLACK:
            pass
        elif sensorCorEsquerda.color() == Color.GREEN:
            robo.stop()
            while sensorCorEsquerda.color() != Color.WHITE:
                robo.drive(-30,0)
            while sensorCorEsquerda.color() != Color.BLACK or sensorCorDireita.color() != Color.GREEN:
                robo.drive(25,13)
                if sensorCorEsquerda.color() == Color.BLACK:
                    robo.stop()
                    break
                elif sensorCorDireita.color() == Color.GREEN:
                    robo.stop()
                    break
            robo.stop()
            if sensorCorEsquerda.color() == Color.BLACK:
                robo.turn(-20)
                robo.straight(60)
                while sensorCorEsquerda.color() != Color.BLACK:
                    robo.drive(0,-45)
            elif sensorCorDireita.color() == Color.GREEN:
                robo.straight(10)
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(0,45)
                robo.turn(-20)
                if sensorCorDireita.color() == Color.GREEN:
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(0,90)
                    robo.straight(-30)

    elif sensorCorDireita.color() == Color.GREEN:
        robo.straight(5)
        robo.stop()
        robo.turn(10)
        if sensorCorDireita.color() == Color.BLACK:
            pass
        elif sensorCorDireita.color() == Color.GREEN:
            robo.stop()
            while sensorCorDireita.color() != Color.WHITE:
                robo.drive(-30,0)
            while sensorCorDireita.color() != Color.BLACK or sensorCorEsquerda.color() != Color.GREEN:
                robo.drive(25,-13)
                if sensorCorDireita.color() == Color.BLACK:
                    robo.stop()
                    break
                elif sensorCorEsquerda.color() == Color.GREEN:
                    robo.stop()
                    break
            robo.stop()
            if sensorCorDireita.color() == Color.BLACK:
                robo.turn(20)
                robo.straight(60)
                while sensorCorDireita.color() != Color.BLACK:
                    robo.drive(0,45)
            elif sensorCorEsquerda.color() == Color.GREEN:
                robo.straight(10)
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(0,-45)
                robo.turn(20)
                if sensorCorEsquerda.color() == Color.GREEN:
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(0,-90)
                    robo.straight(-30)
    
    robo.drive(90,0)

    # obstaculo
    if ultraSonico.distance() < 50:
        voltaObstaculo()
