@echo off
TITLE TaigaRobot
:: Enables virtual env mode and then starts taiga
env\scripts\activate.bat && py -m TaigaRobot
