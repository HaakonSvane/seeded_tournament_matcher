## Seeded tournament elimination matcher
The algorithm outputs integers representing the seeding of players in an order
such that advantage is given to the higher seeded players. This means that
for any given matchup, if the highest seeded player of the two wins, the 
bracket is  constructed such that player 1 meets player 2 in the finals.
Another way of putting it is that the sum of the seedings in any match
is always equal to n + 1, where n is the number of participants for the round. 

__Note that the algorithm only works for integers that satisfy 2^k, where k is
any natural number.__ While this may perhaps seem like a gruesome limitaiton of
the algorithm, a tournament bracket system of any size will always be reduced
to such a number after the first round of byes are handled.
   
