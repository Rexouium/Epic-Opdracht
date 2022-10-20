#for i in range(5):
 #   robotArm.grab()
 #   robotArm.moveLeft()
 #   robotArm.drop()
 #   robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:

from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(3):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()