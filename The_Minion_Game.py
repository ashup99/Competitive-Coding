'''
Solution to a problem on HackerRank
https://www.hackerrank.com/challenges/the-minion-game/problem
'''





def minion_game(string):
    # your code goes here
    S = string.strip()
    S_length = len(S)
    player1, player2 = 0,0

    for i in xrange(S_length):
        if S[i] in "AEIOU":
            player1 += S_length - i
        else:
            player2 += S_length - i        
            
    if player1 > player2:
        print "Kevin", player1
    elif player1 < player2:
        print "Stuart", player2
    else:
        print "Draw"

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
