# Init Variables
# the shit that gonna get replaced
theMatrix = ""
system = ""
Neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""
protect = ""

profession = ["", "", "", ""]
adj = ["", ""]

# Get input from user
# This is what text will pop up and the text they will read and rspond to
print("Welcome User!")
print("Lets Play a Game of MadLibs!")
neo = input("Please Share With Me Your Name?\n")

print(f"Hello {neo}! Are you ready?")
theMatrix = input("What is something you would like to know more about?\n")

print(f"Oooooh! you want to know more about {theMatrix} huh?")
print(f"Okay, Well first tell me what you already know about {theMatrix}.")
system = input(f"What noun would you categorize {theMatrix} as?\n")

enemy = input(f"Give me and oppsing noun to {system}\n")

inside = input(f"Now give me any relaxing noun (present tense)\n")

print(f"Ok now I need 4 professions relating to {system}")

for i in range(len(profession)):
    profession[i] = input(f"profession (plural) {i+1} / {len(profession)}\n")

save = input(f"What do we do with baby seals?\n")

print(
    f"Well you have done a fine job so fair but now we have a shortage in baby seals we have now days do to {save}"
)
unplugged = input(f"how do we turn of a light when the swith wont work?\n")

print(f"If your want to {save} the baby seals how would you go about doing it?")
fight = input(f"Please do tell.\n")

print(f"and last, but not least")
protect = input(
    f"If you were not planning on {save} the baby seals what would you do?\n"
)

for i in range(len(adj)):
    adj[i] = input(f"adjective (2) {i+1} / {len(adj)}\n")

# Init Story
# This is the story and the words that are going to be replaced with the input from the user
madlibsStory = (
    f"{theMatrix} is a {system}, {Neo}. That {system} is our {enemy}. "
    + f"But when you're {inside}, you look around, what do you see? "
    + f"{profession[0]}, {profession[1]}, {profession[2]}, {profession[3]}. The very minds "
    + f"of the people we are trying to {save}. But until we do, "
    + f"these people are still a part of that {system} and that makes "
    + f"them our enemy. You have to understand, most of these people "
    + f"are not ready to be {unplugged}. And many of them are so {adj[0]}, "
    + f"so hopelessly {adj[1]} on the {system}, that they will {fight} to {protect} it."
)

# Print Story
# And a warm thanks
print(madlibsStory)
print("Thanks for playing!")
input()
