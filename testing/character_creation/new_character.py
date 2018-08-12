name = input("Enter character's name: ")
race = input("Enter character's race: ")
size = input("Enter the physical size of your character [small/medium/large/huge]: ")
while True:
    if size.lower() == "small" or size.lower() == "medium" or \
            size.lower() == "large" or size.lower() == "huge":
        break
physical_traits = input("Enter up to two physical traits for your character: ")
social_traits = input("Enter up to two social traits for your character: ")
secret = input("Enter your character's secret: ")
