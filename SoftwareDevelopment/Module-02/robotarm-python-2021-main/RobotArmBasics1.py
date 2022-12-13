from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:

Rijen = 9

while Rijen != 0:
    robotArm.grab()
    Kleur = robotArm.scan()
    if Kleur != "red":
        robotArm.drop()
        robotArm.moveRight()
        Rijen -= 1
    else:
        for i in range(Rijen):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(Rijen-1):
            robotArm.moveLeft()
        Rijen -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()