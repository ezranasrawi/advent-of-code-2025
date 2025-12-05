import os

def getinput(day, example):
    
    prefix = 'example-' if example else 'input-'
    filepath = os.path.join(os.getcwd(), 'input', f'{prefix}{day}.txt')

    with open(filepath, "r") as input_file:
        data = [line.rstrip('\n') for line in input_file]

    return data if len(data) > 1 else data[0]