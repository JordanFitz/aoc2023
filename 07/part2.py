#!/bin/python3

NONE = []
ONE_PAIR = [2]
TWO_PAIR = [2,2]
THREE_OF_A_KIND = [3]
FULL_HOUSE = [2,3]
FOUR_OF_A_KIND = [4]
FIVE_OF_A_KIND = [5]

strengths = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
group_strengths = [
    NONE,
    ONE_PAIR,
    TWO_PAIR,
    THREE_OF_A_KIND,
    FULL_HOUSE,
    FOUR_OF_A_KIND,
    FIVE_OF_A_KIND,
]

def count_jokers(hand):
    result = 0
    for c in hand:
        if c == 'J': result += 1
    return result

def get_joker_groups(hand):
    streak = 1
    groups = []
    for i,curr in enumerate(hand[1:]):
        if curr != 'J': continue
        last = hand[i]
        if curr == last:
            streak += 1
            streak_type = curr
        else:
            if streak > 1:
                groups.append(streak)
            streak = 1
    if streak > 1:
        groups.append(streak)

    if len(groups) == 0 and hand.find('J') != -1:
        return [1]

    return groups

def get_hand_strength(hand):
    orig = hand

    hand = "".join(sorted(list(hand)))
    
    streak = 1
    groups = []
    for i,curr in enumerate(hand[1:]):
        if curr == 'J': continue
        last = hand[i]
        if curr == last:
            streak += 1
        else:
            if streak > 1:
                groups.append(streak)
            streak = 1
    if streak > 1:
        groups.append(streak)

    # g = list(sorted(map(lambda t: t[0], groups)))
    groups.sort()
    jokers = count_jokers(hand)

    if jokers != 0:
        print(hand, groups, jokers)

        orig_g = groups

        if groups == NONE:
            if jokers == 1:
                groups = ONE_PAIR
            if jokers == 2:
                groups = THREE_OF_A_KIND
            if jokers == 3:
                groups = FOUR_OF_A_KIND
            if jokers == 4 or jokers == 5:
                groups = FIVE_OF_A_KIND
        elif groups == ONE_PAIR:
            if jokers == 1:
                groups = THREE_OF_A_KIND
            if jokers == 2:
                groups = FOUR_OF_A_KIND
            if jokers == 3:
                groups = FIVE_OF_A_KIND
        elif groups == TWO_PAIR:
            if jokers == 1:
                groups = FULL_HOUSE
        elif groups == THREE_OF_A_KIND:
            if jokers == 1:
                groups = FOUR_OF_A_KIND
            if jokers == 2:
                groups = FIVE_OF_A_KIND
        elif groups == FOUR_OF_A_KIND:
            if jokers == 1:
                groups = FIVE_OF_A_KIND

        assert groups != orig_g

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
        # print(hands)

        hands.sort(key=lambda h: (h[0],
            get_card_strength(h[1][0]),
            get_card_strength(h[1][1]),
            get_card_strength(h[1][2]),
            get_card_strength(h[1][3]),
            get_card_strength(h[1][4]),
        ))
        # print(hands)

        winnings = 0
        for i, hand in enumerate(hands):
            winnings += (i+1)*hand[2]

        print(winnings)

if __name__ == '__main__':
    main()
