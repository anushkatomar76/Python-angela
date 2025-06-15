TODO-1
Create an empty String called placeholder.
For each letter in the chosen_word, add a _ to placeholder.
So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.
Print out hint.

 Hint 1 
Remember you can use the range() function inside a loop to carry out an action for a particular number of times.
TODO-2

Create an empty string called "display".//
Loop through each letter in the chosen_word//
If the letter at that position matches guess then reveal that letter in the display at that position.
e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
Print display and you should see the guessed letter in the correct position.
But every letter that is not a match is represented with a "_".
 Hint 2 
Remember that the for loop will go through each letter in the chosen_word in order.
You can use that fact to create a new string, appending the letter or an "_".


#step3
DO-1-->
Use a while loop to let the user guess again.
The loop should only stop once the user has guessed all the letters in the chosen_word.
At that point display has no more blanks ("_"). Then you can tell the user they've won.
 Hint 1 
You can use the in keyword to check if a String or List contains a particular item.
e.g. Google: check if a letter is present in a string python

TODO-2
Update the for loop so that previous guesses are added to the display String.
At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.
 Hint 2 
Think about how you can store the matched letters and use an elif to check if a letter has been matched before.



