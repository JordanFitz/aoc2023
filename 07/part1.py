#!/bin/python3

strengths = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
group_strengths = [
    [],
    [2],
    [2,2],
    [3],
    [2,3],
    [4],
    [5]
]

def get_hand_strength(hand):
    orig = hand

    hand = "".join(sorted(list(hand)))
    
    streak = 1
    groups = []
    for i,curr in enumerate(hand[1:]):
        last = hand[i]
        if curr == last:
            streak += 1
        else:
            if streak > 1:
                groups.append(streak)
            streak = 1
    if streak > 1:
        groups.append(streak)

    groups.sort()

    strength = group_strengths.index(groups)

    assert strength != -1
    return strength

def get_card_strength(card):
    return strengths.index(card)

def main():
    with open("input.txt") as input:
        hands = []
        for line in input:
            hand, bid = line.strip().split(" ")
            bid = int(bid)
            hand_strength = get_hand_strength(hand)
            hands.append((hand_strength,hand,bid,))
        print(hands)

        hands.sort(key=lambda h: (h[0],
            get_card_strength(h[1][0]),
            get_card_strength(h[1][1]),
            get_card_strength(h[1][2]),
            get_card_strength(h[1][3]),
            get_card_strength(h[1][4]),
        ))
        print(hands)

        winnings = 0
        for i, hand in enumerate(hands):
            winnings += (i+1)*hand[2]

        print(winnings)

if __name__ == '__main__':
    main()
