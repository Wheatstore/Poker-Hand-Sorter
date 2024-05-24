from collections import Counter

hand = ["3S", "JC", "JD", "3D", "AH"]
straight_hand = ["9H", "8D", "7C", "6S", "5H"]
value_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def initialize_hand(hand):
    converted_order = []
    non_converted_order = hand
    print("Raw Cards:", non_converted_order)
    for i in non_converted_order:
        value = i[0][0]
        suit = i[1]
        if value in value_dict:
            new_value = value_dict[value]

        else:
            new_value = int(value)
        converted_order.append((new_value, suit))
    sorted_cards = sorted(converted_order, key=lambda x: x[0], reverse=True)
    print("Sorted Cards:", sorted_cards)
    return sorted_cards
    
def check_pair_or_two_or_three(hand):
    number_counts_dict = {}
    num_of_pairs = 0
    for value, suit in hand:
        if value in number_counts_dict:
            number_counts_dict[value] += 1
        else:
            number_counts_dict[value] = 1
    
    for i in number_counts_dict:
        if number_counts_dict[i] == 2:
            num_of_pairs += 1
    
    if num_of_pairs == 1:
        return True, 'One pair'
    
    if num_of_pairs == 2:
        return True, "Two Pair"
    
    if num_of_pairs == 3:
        return True, "Three Pair"
    
    else:
        return False

def checkIf_Straight(hand):
    values = []
    for i in hand:
        values.append(i[0])
    
    print(values)
    
    for i in range(4):
        
        if (int(values[i]) - 1) != int(values[i + 1]):
            return False, "Not a straight"
        else: 
            return True, "A straight"
    
converted_order = initialize_hand(hand)
print(check_pair_or_two_or_three(converted_order))
print(checkIf_Straight(converted_order))

