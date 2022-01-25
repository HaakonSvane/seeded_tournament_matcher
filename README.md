## Seeded tournament elimination matcher
The algorithm outputs integers representing the seeding of players in an order
such that advantage is given to the higher seeded players. This means that
for any given matchup, if the highest seeded player of the two wins, the 
bracket is  constructed such that player 1 meets player 2 in the finals.
Another way of putting it is that the sum of the seedings in any match
is always equal to n + 1, where n is the number of participants for the round. 

__Note that the algorithm only works for integers that satisfy 2<sup>k</sup>, where k is
any natural number.__ While this may perhaps seem like a limitaiton of
the algorithm, a tournament bracket system of any size will always be reduced
to such a number after the first round of byes are handled anyways.

### How does it work?

![image](/asset/img/workingsTable.png)

The first thing to consider is that for any number of participants _n_, where n satisfies 
2<sup>k</sup> for any natural number k, the match up player _m_ for a player seeded at place _p_ is given
by m<sub>p</sub> = n - p + 1. For example, for n = 16, p = 1, m<sub>1</sub> = 16.

The algorithm works recursively for each level of a tournament tree (denoted _i_ in the 
illustration). Starting out at the root node (p = 1), it left-traverses the tree until it has reached
the bottom of the tree (when the condition i = k is true). From here, it is trivial to calculate the 
match up player.

### Some interesting notes
For 2<sup>3</sup> = 8 participants, the algorithm generates the following sequence of numbers:
> (1, 8, 4, 5, 2, 7, 3, 6)
> 
For any positive power of two, sequence has some interesting remarks:
1. It resembles the number of sign changes per row in a naturally ordered Hadamard-Walsh matrix shifted by one digit.
2. As a permutation, this sequence is isomorphic to the cyclic group (perhaps obviously). The order of the groups as a
function of the number of participants _n_ is not necessarily trivial. For both n = 8 and n = 16,
the permutation yields a group isomorphic to the cyclic group of order 7, but for n = 4, 32 and 64, 
the group is of order n-1. This needs to be further looked into and verified properly however.
    
