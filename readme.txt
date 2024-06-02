Here we will attempt to explain how the game works...


When our project.py program is first run through the terminal, a welcoming screen will be displayed(Use full screen to completely view our menu) and 
the user will be given three options: 
1) Start, 2) Tutorial and -1) Exit and the user will enter 1 or 2 to proceed and -1) to exit

If the user decides to enter 1) to the program, he/she will be provided with yet another 3 options for game modes (Blind Mode, Hunt Mode and Create custom game)
and another option to return back to the home screen. Enter -1 to return back.

If the user enters either game modes, there will be various options for the topic of the word search, e.g Data Types, Sports, Brands.
Enter -1 to return back.

The user will then be prompted to input the difficulty level, ranging from Easy to Advanced. Easy gives an 8x8 board, while Intermediate
gives a 11x11 board, while Advanced gives a 15x15 board. For all of these difficulty levels, the players are given 5 hints to help them 
win the game...

---> For Blind Mode,
A board will then be printed and the user is expected to search for words on the board with its letters
placed next to each other in the hoirzontal/vertical/diagonal direction. The challenge of the game is to enter the words you spot.
                                Game topic: Data Types
                                ###########################
                                #  b  o  c  i  t  h  f  s #
                                #  o  m  i  u  c  s  z  l #
                                #  o  s  n  h  t  h  i  t #
                                #  l  n  t  d  e  z  a  l #
                                #  e  h  e  r  n  h  t  r #
                                #  a  y  g  u  i  z  m  p #
                                #  n  m  e  p  q  n  m  i #
                                #  f  y  r  f  m  u  g  d #
                                ###########################
                Enter 'boolean' because it lies vertically on the board on the first column
                The letters will be highlighted with blue on the board for distinction.
                Enter H for hints
                Continue entering the remaining words to win the game.
                Once the player has won, the program returns back to the main menu.

---> For Hunt Mode,
A board will be printed and the player is expected to traverse the board using the keys wasd. The current position is marked by the red bolded letter and Entering M 
will turn the letter blue. Entering U undoes the mark and turns the letter back to red. Entering H gives hint, similar to Blind Mode. To find a word, the player must
mark all the letters in the correct order. For example, for the word 'queue', the player must mark q, u, e, u, e in the correct order. 
                                Entered Letters: queue
                                        Found word: queue
                                There are 4 words left to search for!
                        ======================================================
                                ###########################
                                #  y  q  o  n  s  s  c  r #
                                #  a  u  i  t  t  b  v  x #
                                #  a  y  a  r  f  e  a  v #
                                #  c  c  i  g  o  d  o  w #
                                #  k  n  a  r  r  a  y  o #
                                #  g  c  x  o  c  d  m  c #
                                #  e  u  e  u  q  t  u  i #
                                #  m  r  e  g  e  t  n  i #
                                ###########################
                Colors cannot be shown in textfiles, but to receive this message, the player must first traverse
                the board to find the word. Starting from row 1 column 7, we see 'eueuq' which is essentially
                queue in reverse order. The player must traverse to q on row 5 column 7 and mark it, followed by 
                u on row 4 column 7.....e on row 1 column 7. Finally, the player will receive the message above.
                Finish all 5 words to win the game.

                Note that when you are currently in the same position as a blue marked letter, the red bolded letter 
                will not show. Try to move out (wasd) of the blue marked region to see your current position, given by
                the red bolded letter. It is the player's task to keep track of their position in blue marked regions.
Remember, you can press the number 2 again in the main menu to see this tutorial again & again.








