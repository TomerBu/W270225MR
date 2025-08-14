# random password generator:

letter_count = int(input("How many letters: "))

use_lower = input('Use lower case letters y/n: ')
use_upper = input('Use upper case letters y/n: ')
use_digits = input('Use digits y/n: ')
use_punctuation = input('Use punctuation y/n: ')

from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import choice, randint

ascii_bank = ''
if use_lower == 'y':
    ascii_bank += ascii_lowercase

if use_upper == 'y':
    ascii_bank += ascii_uppercase

if use_digits == 'y':
    ascii_bank += digits

if use_punctuation == 'y':
    ascii_bank += punctuation


if not ascii_bank:
    print('You must select at least one character type.')
    exit()


password = ''

for _ in range(letter_count):
    password += choice(ascii_bank)

print(password)
