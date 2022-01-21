# Wordle
If you haven't heard of Wordle, go check out the webpage: https://www.powerlanguage.co.uk/wordle/

# Dictionaries
Version 2 uses Scrabble Dictionaries found here: https://www.wordgamedictionary.com/word-lists/

Version 1 uses a Github word list that I stripped out all 5 letter words: https://github.com/dwyl/english-words

# How To Use
You will first be asked how many letters you wish to solve for.  This program supports 2 to 15 letters (see word_list folder).  You can enter a number, or hit enter for the default value of 5 (based on wordle).  The solver will then check the dictionary for the best 5 words to use.  After entering a word, you must tell the solver the results:

>Enter Known Leters and Place (**a**):

Format the string based on where you know there are letters.  If there are none, hit enter or type in ***** (for 5 letter words).
Example: r***e

>Enter Known Letters in Unknown Places:

Enter the letters you know are in the answer, but are in the wrong place. If there are none, hit enter
Example: s

>Enter wrong locations for Known Letters:

Enter a string based on where you know letters can't be.  If there are none, hit enter or type in ***** (for 5 letter words).
Example: ***s*

>Enter Exiled Letters: ai

Enter the letters you have guessed and know are not in the word.  If there are none, hit enter.
Example: ai

The program will eliminate all words not matching your criteria.  It will reassess the words, and give 5 new suggestions.  The program it sequential, and won't include the words already removed from the previous round.  This can simplify entries as you only need to enter the newest data.  You can enter all the data, it won't affect the results.
