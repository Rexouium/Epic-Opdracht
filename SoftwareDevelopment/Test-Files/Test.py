print("Welcome to the Fursona Maker!")

# Get the fursona's attributes from the user
print("Enter your fursona's species:")
species = input()
print("Enter your fursona's fur color:")
fur_color = input()
print("Enter your fursona's eye color:")
eye_color = input()

# Generate the fursona description
fursona = "Your fursona is a {0} with {1} fur and {2} eyes.".format(species, fur_color, eye_color)

# Print the fursona description
print(fursona)
