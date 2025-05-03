''' Make a program that reads a sentence from the keyboard and shows:
- How many times the letter 'R' appears
- In which position it appears the first time
- In which position it appears the last time '''

phrase = str(input('Enter your phrase: ')).upper().strip()
print('The letter "R" appears {} times in the sentence'.format(phrase.count('R')))
print('The letter "R" first appears in position {}'.format(phrase.find('R')+1))
print('The letter "R" last appears in position {}'.format(phrase.rfind('R')+1))
