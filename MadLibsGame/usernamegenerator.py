from random import choice, randint


adjectives = ['lazy', 'speedy', 'wriggly', 'smart', 'blue']
nouns = choice(adjectives)

animals = ['cat', 'dog', 'fish', 'beetle', 'duck', 'seagull']
creature = choice(animals)

foo = randint (1, 9)
num1 = str(foo)

oof = randint (1, 9)
num2 = str(oof)

username = (nouns+creature+num1+num2)

print ('Username is', username)
