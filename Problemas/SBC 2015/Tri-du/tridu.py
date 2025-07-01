# https://judge.beecrowd.com/en/problems/view/1933

cards = [int(c) for c in input().split()]
if cards[0] == cards[1]: print(cards[0])
else: print(max(cards))
