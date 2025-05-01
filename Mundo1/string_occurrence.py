''' Faça um programa que leia um frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'R'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a última vez '''

phrase = str(input('Enter your phrase: ')).upper().strip()
print('The letter "R" appears {} times in the sentence'.format(phrase.count('R')))
print('The letter "R" first appears in position {}'.format(phrase.find('R')+1))
print('The letter "R" last appears in position {}'.format(phrase.rfind('R')+1))
