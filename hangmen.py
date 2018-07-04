import random

words = ["aspect","internal","growth","conversation","informal","alive","surely",
"publish","apply","sensitive","club","master","theirs","waste","introduction","illustrate",
"bored","living","nonsense","qualify"]

word1 = random.choice(words)
word = list(word1)
lenght = len(word)
    
def guess(word,letter, lenght, lives, guessed_untill_now,dashes):
    repeat_of_letter = 0
    for i in range(0, lenght):
        if letter==word[i]:
            dashes[i]=letter
            repeat_of_letter += 1 

    if repeat_of_letter==0:
        lives = lives - 1
    guessed_untill_now += repeat_of_letter

    return(guessed_untill_now, lives)

def main():
    dashes = list("_"*lenght)
    number_of_guessed_letters = 0
    lives = 6   

    while(lives>0):
        letter = input("Please choose a letter.")
        number_of_guessed_letters, lives= guess(word,letter,lenght,lives,number_of_guessed_letters,dashes)
        if lives==0: 
            print("You lost  (the word was: "+str(word))
        elif number_of_guessed_letters==lenght:
            print("You won")
            break
        else:
         print("You have " + str(lives) + " lives left")
         print(dashes)

main()