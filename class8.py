# ADVANCED STRING

my_name = 'Nadim Chowdhury'
print(my_name[0])
print(my_name[-1])

sentence = 'My name is NADIM CHOWDHURY'
print(sentence[:4])
print(sentence[6:])

sentence_split = sentence.split(' ')
print(sentence_split)
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said 'Give me a car.'"
print(quote)
quote = 'He said \'Give me a bike.\''
print(quote)

too_much_space = '          Hello             '
print(too_much_space.strip())

print('A' in 'Apple') # True
print('a' in 'Apple') # False

letter = 'A'
word = 'Apple'
print(letter.lower() in word.lower())

movie = 'Ghost Rider'
print('My favourite movie is {}'.format(movie))
print('My favourite movie is %s' % movie)
print(f'My favourite movie is {movie}')
