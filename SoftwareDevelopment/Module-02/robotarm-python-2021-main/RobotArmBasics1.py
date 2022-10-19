# Robotarm bibliotheek inladen
from shutil import move
from RobotArm import RobotArm
            
# De robotarm opstarten in een bepaald level, bijvoorbeeld 'exercise 1'
robotArm = RobotArm('exercise 1')
            
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
robotArm.grab()
MoveR1 = 1
while MoveR1 < 6:
    robotArm.moveRight()
    if MoveR1 > 5:
        break
    else:
        MoveR1 += 1
robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()