from random import choice

hangman_words = [
	"apple", "banana", "cherry", "grapefruit", "strawberry", "watermelon", "pineapple", "mango", "peach", "apricot", "plum", "kiwi", "lemon", "lime", "orange", "pear", "fig", "date", "melon", "papaya", "guava", "blueberry", "raspberry", "blackberry", "coconut", "avocado", "pomegranate", "nectarine", "passionfruit", "dragonfruit", "lychee", "persimmon", "tangerine", "cantaloupe", "currant", "cranberry", "kumquat", "starfruit", "jackfruit", "durian", "olive", "quince", "chestnut", "hazelnut", "walnut", "almond", "cashew", "pecan", "macadamia", "pumpkin", "carrot", "tomato", "potato", "onion", "garlic", "broccoli", "cauliflower", "lettuce", "spinach", "cabbage", "celery", "radish", "turnip", "beet", "zucchini", "squash", "eggplant", "pepper", "cucumber", "pea", "bean", "corn", "rice", "wheat", "barley", "oat", "rye", "buckwheat", "millet", "sorghum", "quinoa", "spelt", "teff", "amaranth"
]

#1)  random word:
chosen_word = choice(hangman_words)
print("chosen word:", chosen_word)


#2) list of underscores
display = list("_"*len(chosen_word))
 
while "_" in display:
    print(display)
    guess = input("Enter a letter:").lower()

    if guess not in chosen_word:
        print("wrong")
        continue


    # loop over the word
    for i in range(len(chosen_word)):
        # if index of guess is in word
        if guess == chosen_word[i]:
            # show it:
            display[i] = guess


print('you guessed it', display)
