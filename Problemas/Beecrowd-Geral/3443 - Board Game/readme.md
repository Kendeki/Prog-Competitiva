# Board game

Danilo loves board games. Every weekend he meets his friends to play. However, after years of playing the same classic board games, he grew tired of them and hence decided to create his own game.  

Danilo’s game starts with T tokens on the board, which can be seen as points in the twodimensional plane. There are P players that take a single turn each. In their turn, each player picks a card from a deck. The card describes a straight line, and the player gets all the tokens located strictly below this line. Tokens received by a player do not return to the board. Note that a token located at (X, Y) is strictly below a line y = Ax + B if and only if Y < AX + B.  

Given the list of cards, your task is to find which tokens each player receives.  

###### **Input**  

The first line contains an integer T (1 ≤ T ≤ 105) indicating the number of tokens on the board. Tokens are identified by distinct integers from 1 to T. For i = 1, 2, ... , T, the i-th of the next T lines contains two integers Xi and Yi (−109 ≤ Xi , Yi ≤ 109), denoting the coordinates of the token. No two tokens have the same location.  

The next line contains an integer P (1 ≤ P ≤ 105) representing the number of players in the game. Players are identified by distinct integers from 1 to P, according to the order they take turns. For i = 1, 2, ... , P, the i-th of the next P lines contains two integers Ai and Bi (−109 ≤ Ai , Bi ≤ 109), indicating that the line in the card picked by player i is y = Aix+Bi.  

###### **Output**  

Output P lines. For i = 1, 2, ... , P, the i-th line must contain an integer Ki indicating the number of tokens that player i receives, followed by Ki integers identifying those tokens in ascending order.