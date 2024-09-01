import random

def randomIntByRange(a, b):
    return random.randint(a, b)

def randomFloat():
    return random.random()

def setSeed(seed):
    random.seed(seed)
    return f'Ты серьёзно решил посмотреть сид рандома через print? Ну ладно вот: {seed}'

def randIntByRange(a, b):
    return random.randrange(a, b)

def randomFloat_From_Zero_To_One():
    return random.random()


