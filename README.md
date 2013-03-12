This was my final project for my Algorithmic Game Theory class.

The idea behind it was to create a Blackjack card counting simulation that demonstrated some of the strategy utilized by the famous MIT Blackjack team.

The GUI displays four tables, each with a player betting the table minimum and a label keeping track of the current count. There is also a label to keep track of the current bankroll. The count is calculated as follows: +1 for any 2, 3, 4, 5, or 6, -1 for any 10, J, Q, K, or A, and +0 for any 7, 8, or 9. When the count goes above 10 (when the player's odds of winning a given hand are good), a "shark" steps in and bets the table maximum. The players all play with proven optimal strategy, where in the long run they should win just under 50% of the hands. With card counting, in the long run, this type of team playing should produce profits by betting high when the chances of winning a given hand is above 50%.

Here is the widely-accepted documented Blackjack strategy that I used for implementation:
http://www.blackjack-strategycard.com/images/Blackjack%20Strategy%20Chart%20Multi-Deck.gif

=========
