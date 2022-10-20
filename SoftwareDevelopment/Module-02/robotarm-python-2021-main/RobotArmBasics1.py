#for i in range(5):
 #   robotArm.grab()
 #   robotArm.moveLeft()
 #   robotArm.drop()
 #   robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:


from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
for i in range(7):
    robotArm.moveRight()

for i in range(7):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()

robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()