import random

def dict_gen(q, a):
    result = dict(question=q, answer=a)
    return result

def card_flip():
    while True:
        card = random.choice(cards)
        yield card['question']
        yield card['answer']

with open('card_data.txt', 'r') as f:
    cards = []
    for line in f:
        clean_line = line.strip('\n')
        q,a = clean_line.split(' # ')
        line_dict = dict_gen(q, a)
        cards.append(line_dict)

flip = card_flip()

while True:
    prompt = input('Hit "n" key and "enter" to advance. Just hit "enter" key to quit: ')
    if prompt != 'n':
        break
    print('\n')
    print(next(flip))
    print('\n')
