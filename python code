from pip._vendor.distlib.compat import raw_input
import random

py_rat = {
    'photo': '<:3}~~~',
    'name': 'Bisco',
    'age': 2,
    'weight': .8,
    'hungry': True,
    'thirsty': True,
    'tired': False,
    'bisco_phrases' : ['>Bisco chitters back at you.', '>Bisco boggles happily.',
                       '>Bisco sqeaks in surprise.'],
    'user_phrases' : ['You attempt to talk to Bisco about the weather.',
                    'You attempt to talk to Bisco about recent comptroller election in your area.',
                    'You attempt to initiate a conversation about Warhammer 40k'],
}

pypet = py_rat

def startup_pypet():
    print("Welcome to Pypet!")

def commands_list():
    print("You can interact with your PyPet with a few commands listed below.")
    print(" '>stats' "
          " '>pet' "
          " '>feed' "
          " '>water' "
          " '>chat' "
          " '>play' "
          " '>rest' ")

def pypet_stats():
    print("Hello, it's " + py_rat['name'])
    print(py_rat['name'] + " weighs " + str(py_rat['weight']) + " pounds.")

    if py_rat['hungry']:
        print("Your PyPet is hungry.")

    if py_rat['thirsty']:
        print("Your PyPet is thirsty.")

    if py_rat['tired']:
        print("Your PyPet is tired and would like to go to bed.")

    else:
        print(">Bisco sqeaks in content.")

def play_activities():
    print(" '>practice tricks' "
          " '>pull out 'The Tube''"
          " '>obstacle course'")

startup_pypet()
commands_list()

terminate = False

while not terminate:
    print("------------------")

    user_input = raw_input('> ')

    if user_input == "quit":
        terminate = True

    elif user_input == "stats":
        pypet_stats()

    elif user_input == "feed":
        print("Your PyPet nibbles on the food you offer it.")
        py_rat['weight'] = py_rat['weight'] + .15
        py_rat['hungry'] = False

    elif user_input == "water":
        print("Your PyPet happily drinks the water you provide.")
        py_rat['weight'] = py_rat['weight'] + .10
        py_rat['thirsty'] = False

    elif user_input == "chat":
        print(random.choice(py_rat['user_phrases']))
        print(random.choice(py_rat['bisco_phrases']))

    elif user_input == "pet":
        print(" Your PyPet starts to boggle in excitement.")

    elif user_input == "play":
        print("Your Pypet is excited to play with you. What would you like to play?")
        play_activities()

    elif user_input == "practice tricks":
        print("You practice some basic tricks with Bisco, after a while they grow tired and stop playing.")
        py_rat['tired'] = True

    elif user_input == "pull out 'The Tube'":
        print("You pull out a crinkly tube from the closet and place it on the floor. "
              "Bisco runs through it happily until running out of energy")
        py_rat['tired'] = True

    elif user_input == "obstacle course":
        print("You practice some basic tricks with Bisco, after a while they grow tired and stop playing.")
        py_rat['tired'] = True

    elif user_input == "rest":
        print("You fluff Bisco's bed stuffing and turn off the light for Bisco to go to bed. "
              "You'll check on them in some time.")
        py_rat['tired'] = False
        hungry = True
        py_rat['thirsty'] =True
        py_rat['weight'] = py_rat['weight'] - .25

    else:
        print("Sorry, your PyPet doesn't understand what you want it to do!")


print("Goodbye!")
