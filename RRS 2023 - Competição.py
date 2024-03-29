#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from AreaResgate import *


EV3 = EV3Brick()
LEFT_ENGINE = Motor(Port.A, gears=[24, 24, 24 , 24, 24])
RIGHT_ENGINE = Motor(Port.B, gears=[24, 24, 24 , 24, 24])
OPEN_CLOSE_CLAW_ENGINE = Motor(Port.C)
CURVE_ENGINE = Motor(Port.D)
LEFT_COLOR_SENSOR = ColorSensor(Port.S1)
RIGHT_COLOR_SENSOR = ColorSensor(Port.S2)
ROBOT = DriveBase(LEFT_ENGINE, RIGHT_ENGINE, wheel_diameter=53, axle_track=225)

GREEN_COLOR = Color.GREEN
BLACK_COLOR = Color.BLACK
WHITE_COLOR = Color.WHITE

ULTRASONIC = UltrasonicSensor(Port.S3)

def testeTrueGreen(sensor):
    ROBOT.drive(0,0)
    AMOUNT_OF_TESTS = 300
    colorList = []
    controlerAddColorToList=0
    controlerModaColor=0
    green = 0
    black = 0

    while controlerAddColorToList!=AMOUNT_OF_TESTS:
        colorList.append(sensor.color())    
        controlerAddColorToList += 1
    while controlerModaColor < len(colorList):
        if colorList[controlerModaColor] == GREEN_COLOR:
            green += 1
        elif colorList[controlerModaColor] == BLACK_COLOR:
            black += 1
        controlerModaColor += 1
    
    if green > black:
        return True
    else:
        ROBOT.straight(-10)
        return False


while True:
    ROBOT.drive(65,0)

    if LEFT_COLOR_SENSOR.reflection() > 99 or RIGHT_COLOR_SENSOR.reflection() > 99:
        ROBOT.drive(0,0)
        EV3.speaker.beep()
        area_resgate()

    if LEFT_COLOR_SENSOR.color() == GREEN_COLOR:
        ROBOT.drive(0,0)
        if testeTrueGreen(LEFT_COLOR_SENSOR)==True:
            while LEFT_COLOR_SENSOR.color() != WHITE_COLOR:
                ROBOT.drive(-40,0)
            while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                ROBOT.drive(40,25)
                if RIGHT_COLOR_SENSOR.color() == GREEN_COLOR:
                    break
                elif LEFT_COLOR_SENSOR.color() == BLACK_COLOR:
                    while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                        ROBOT.drive(70,0)
                    ROBOT.turn(-40)
                    while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                        ROBOT.drive(90,0)
                    while LEFT_COLOR_SENSOR.color() != WHITE_COLOR:
                        ROBOT.drive(90,25)
                    while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                        ROBOT.drive(0,-40)
                    break
            ROBOT.drive(0,0)
            if RIGHT_COLOR_SENSOR.color() == GREEN_COLOR:
                ROBOT.straight(-10)
                while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                    ROBOT.drive(0,80)
    elif RIGHT_COLOR_SENSOR.color() == GREEN_COLOR:
        ROBOT.drive(0,0)
        if testeTrueGreen(RIGHT_COLOR_SENSOR)==True:
            while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
                ROBOT.drive(-40,0)
            while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                ROBOT.drive(40,-25)
                if LEFT_COLOR_SENSOR.color() == GREEN_COLOR:
                    break
                elif RIGHT_COLOR_SENSOR.color() == BLACK_COLOR:
                    while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                        ROBOT.drive(70,0)
                    ROBOT.turn(40)
                    while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                        ROBOT.drive(90,0)
                    while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
                        ROBOT.drive(90,-25)
                    while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                        ROBOT.drive(0,40)
                    break
            ROBOT.drive(0,0)
            if LEFT_COLOR_SENSOR.color() == GREEN_COLOR:
                ROBOT.straight(-10)
                while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                    ROBOT.drive(0,-80)

    if LEFT_COLOR_SENSOR.color() == BLACK_COLOR:
        while LEFT_COLOR_SENSOR.color() != WHITE_COLOR:
            if RIGHT_COLOR_SENSOR.color() == BLACK_COLOR:
                ROBOT.turn(20)
                while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                    ROBOT.drive(0, 50)
                ROBOT.straight(30)
                while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                    ROBOT.drive(40, -50)
                while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
                    ROBOT.drive(30, 60)
            ROBOT.drive(5, -30)
    elif RIGHT_COLOR_SENSOR.color() == BLACK_COLOR:
        while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
            if LEFT_COLOR_SENSOR.color() == BLACK_COLOR:
                ROBOT.turn(-20)
                while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
                    ROBOT.drive(0, -50)
                ROBOT.straight(30)
                while LEFT_COLOR_SENSOR.color() != BLACK_COLOR:
                    ROBOT.drive(40, 50)
                while LEFT_COLOR_SENSOR.color() != WHITE_COLOR:
                    ROBOT.drive(30, -60)
            ROBOT.drive(5, 30)

    if ULTRASONIC.distance() < 65:
        ROBOT.drive(0,0)
        if LEFT_COLOR_SENSOR.color() == BLACK_COLOR:
            while LEFT_COLOR_SENSOR.color() != WHITE_COLOR:
                ROBOT.drive(0,-25)
        elif RIGHT_COLOR_SENSOR.color() == BLACK_COLOR:
            while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
                ROBOT.drive(0,25)

        ROBOT.turn(90)
        ROBOT.straight(140)
        ROBOT.turn(-45)
        ROBOT.straight(140)
        ROBOT.turn(-45)
        ROBOT.straight(220)
        ROBOT.turn(-45)
        ROBOT.straight(140)
        while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
            ROBOT.drive(50,-18)
        while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
            ROBOT.drive(50,0)
        ROBOT.straight(10)
        while RIGHT_COLOR_SENSOR.color() != BLACK_COLOR:
            ROBOT.drive(0,50)
        while RIGHT_COLOR_SENSOR.color() != WHITE_COLOR:
            ROBOT.drive(0,50)
        EV3.speaker.beep()
