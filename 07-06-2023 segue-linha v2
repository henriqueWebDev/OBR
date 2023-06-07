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

travaResgate = False

#tem  4 motor médio  
# trabalhar no verde

def confirmarVerde(sensor):
    robo.drive(0,0)
    listaCor = []
    green = 0
    black = 0
    cont1=0
    cont2=0
    while cont1!=200:
        listaCor.append(sensor.color())    
        cont1 += 1
    while cont2 < len(listaCor):
        if listaCor[cont2] == Color.GREEN:
            green += 1
        elif listaCor[cont2] == Color.BLACK:
            black += 1
        cont2 += 1
    
    print('verde',green)
    print('preto',black)
    print('_________')
    if green > black:
        return True
    elif black > green:
        return False

while True:
    robo.drive(70,0)

    # Verificação verde
    if sensorCorEsquerda.color() == Color.GREEN:
        robo.drive(0,0)
        if confirmarVerde(sensorCorEsquerda)==True:
           # True verde
            while sensorCorEsquerda.color() != Color.WHITE:
                robo.drive(-40,0)
            while sensorCorEsquerda.color() != Color.BLACK:
                robo.drive(40,25)
                if sensorCorDireita.color() == Color.GREEN:
                    break
                elif sensorCorEsquerda.color() == Color.BLACK:
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(70,0)
                    robo.turn(-40)
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(90,0)
                    while sensorCorEsquerda.color() != Color.WHITE:
                        robo.drive(90,0)
                    while sensorCorEsquerda.color() != Color.BLACK:
                        robo.drive(0,-40)
                    break
            robo.drive(0,0)
            if sensorCorDireita.color() == Color.GREEN:
                while sensorCorDireita.color() != Color.BLACK:
                    robo.drive(0,80)
        else: 
            # False verde
            robo.straight(-20)

    elif sensorCorDireita.color() == Color.GREEN:
        robo.drive(0,0)
        if confirmarVerde(sensorCorDireita)==True:
            # True verde
            while sensorCorDireita.color() != Color.WHITE:
                robo.drive(-40,0)
            while sensorCorDireita.color() != Color.BLACK:
                robo.drive(40,-25)
                if sensorCorEsquerda.color() == Color.GREEN:
                    break
                elif sensorCorDireita.color() == Color.BLACK:
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(70,0)
                    robo.turn(40)
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(90,0)
                    while sensorCorDireita.color() != Color.WHITE:
                        robo.drive(90,0)
                    while sensorCorDireita.color() != Color.BLACK:
                        robo.drive(0,40)
                    break
            robo.drive(0,0)
            if sensorCorEsquerda.color() == Color.GREEN:
                while sensorCorEsquerda.color() != Color.BLACK:
                    robo.drive(0,-80)
        else: 
            # False verde
            robo.straight(-20)

    #Verficia preto
    if sensorCorEsquerda.color() == Color.BLACK:
        while sensorCorEsquerda.color() != Color.WHITE:
            if sensorCorDireita.color() == Color.BLACK:
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(0,40)
                robo.straight(60)
                while sensorCorDireita.color() != Color.BLACK:
                    robo.drive(0,-70)
                while sensorCorDireita.color() != Color.WHITE:
                    robo.drive(0,40)
            elif sensorCorEsquerda.color() == Color.GREEN:
                robo.drive(0,0)
                robo.straight(-10)
                break
            robo.drive(0,-40)
    elif sensorCorDireita.color() == Color.BLACK:
        while sensorCorDireita.color() != Color.WHITE:
            if sensorCorEsquerda.color() == Color.BLACK:
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(0,-40)
                robo.straight(60)
                while sensorCorEsquerda.color() != Color.BLACK:
                    robo.drive(0,70)
                while sensorCorEsquerda.color() != Color.WHITE:
                    robo.drive(0,-40)
            elif sensorCorDireita.color() == Color.GREEN:
                robo.drive(0,0)
                robo.straight(-10)
                break
            robo.drive(0,40)

    # Verificação área de resgate
    if (sensorCorEsquerda.reflection() > 99 or sensorCorDireita.reflection() > 99):
        robo.drive(0,0)
        ev3.speaker.beep()
