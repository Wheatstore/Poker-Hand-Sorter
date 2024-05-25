from collections import Counter

hand1 = ["3S", "JC", "JD", "3D", "AH"]
hand = ["AS", "AD", "2H", "5H", "6C"]
straight_hand = ["9H", "8D", "7C", "6S", "5H"]
value_dict = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

#function to sort and initialize an input
def initialize_hand(hand):
    converted_order = []
    non_converted_order = hand
    print("Raw Cards:", non_converted_order)
    #goes through each variable in the raw data of a list
    for i in non_converted_order:
        #the value or the number is the first index of the first index
        value = i[0][0]
        suit = i[1]
        
        #if a value is a letter the new values is the corresponding value in the value_dict
        if value in value_dict:
            new_value = value_dict[value]

        #otherwise the new value is just the old value but as a number
        else:
            new_value = int(value)
        #add these to a new list that is filtered.
        converted_order.append((new_value, suit))
    #sort this new list from the highest first index or number value to the lowest
    sorted_cards = sorted(converted_order, key=lambda x: x[0], reverse=True)
    print("Sorted Cards:", sorted_cards)
    return sorted_cards
    
def check_pariring(hand):
    #the total number of count
    number_counts_dict = {}
    num_of_pairs = 0
    #iterate through the the filtered hand that we were given
    for value, suit in hand:
        #if one of these values are in the dict than we just modify it so that we add plus one to the value
        if value in number_counts_dict:
            number_counts_dict[value] += 1
        
        #otherwise we initialize it so that the value is 1 
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
    
    if num_of_pairs == 4:
        return True, "Four of a kind"
    
    else:
        return False
#function to check if the hand is a straight meaning that each value is consecutive
def checkIf_Straight(hand):
    #add all solely the values to a new function called vaules
    values = []
    for i in hand:
        values.append(i[0])
    #housekeeping
    print(values)
    
    #iterate 4 times
    for i in range(4):
        #if the value of the current index minus 1 is not equal to its next index because it is descending it is not a straight
        if (int(values[i]) - 1) != int(values[i + 1]):
            return False, "Not a straight"
        else: 
            return True, "A straight"

#to check if it is a flush meaning that all suits are the same the process is pretty simple example it has been optimzed
#TOdo, optimize the check if straight function
def check_flush(hand):
    #make a new list called solely suits
    suits = list((i[1])for i in hand)
    #if the number of suits of the first element is not equal to the total lenght of the array the array is not all the same
    if suits.count(suits[0]) == len(suits):
        return True, "is a flush"
    else:
        return False, "Not a flush"  

def check_straightFlush(hand):
    if check_flush(hand) and checkIf_Straight(hand) == True:
        return True, "Is a straight Flush"
    else:
        return False, "Not a straight Flush"

def check_royale_flush(hand):
    is_flush = check_flush(hand)
    royal_flush = [14, 13, 12, 11, 10]
    compare_list = [i[0] for i in hand]
    if royal_flush == compare_list:
        return True, "Royale Flush!"
    else:
        return False, "Not a royale flush"  

        
#place to run the functions in an organized way
converted_order = initialize_hand(hand)
print(check_pariring(converted_order))
print(checkIf_Straight(converted_order))
print(check_flush(converted_order))
print(check_straightFlush(converted_order))
print(check_royale_flush(converted_order))

