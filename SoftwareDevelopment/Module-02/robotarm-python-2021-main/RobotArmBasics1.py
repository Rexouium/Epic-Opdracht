from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for i in range(7):
    robotArm.moveRight()

for i in range(8):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    if i == 8:
        print()
    elif i < 8:
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()