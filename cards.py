def get_deck():
    deck = [ [1,'hearts','ace'], [2, 'hearts','2'],
         [3,'hearts','3'], [4,'hearts','4'],
         [5,'hearts','5'], [6,'hearts','6'],
         [7,'hearts','7'],[8,'hearts','8'],
         [9,'hearts','9'], [10,'hearts','10'],
         [11,'hearts','jack'], [12,'hearts','queen'],
         [13,'hearts','king'],
         [1,'diamonds','ace'], [2, 'diamonds','2'],
         [3,'diamonds','3'], [4,'diamonds','4'],
         [5,'diamonds','5'], [6,'diamonds','6'],
         [7,'diamonds','7'], [8,'diamonds','8'],
         [9,'diamonds','9'], [10,'diamonds','10'],
         [11,'diamonds','jack'], [12,'diamonds','queen'],
         [13,'diamonds','king'],
         [1,'spades','ace'], [2, 'spades','2'],
         [3,'spades','3'], [4,'spades','4'],
         [5,'spades','5'], [6,'spades','6'],
         [7,'spades','7'], [8,'spades','8'],
         [9,'spades','9'], [10,'spades','10'],
         [11,'spades','jack'], [12,'spades','queen'],
         [13,'spades','king'],
         [1,'clubs','ace'], [2, 'clubs','2'],
         [3,'clubs','3'], [4,'clubs','4'],
         [5,'clubs','5'], [6,'clubs','6'],
         [7,'clubs','7'], [8,'clubs','8'],
         [9,'clubs','9'], [10,'clubs','10'],
         [11,'clubs','jack'], [12,'clubs','queen'],
         [13,'clubs','king']]
    return deck

def get_card(deck):
    return deck.pop(0)

def get_score(hand):
    score = 0
    for card in hand:
        if card[0] >= 2 and card[0] <= 10:
            score += card[0]
        elif card[0] == 1:
            if (score + 11) > 21:
                score += 1
            else:
                score += 11
        elif card[0] == 11 or card[0] == 12 or card[0] == 13:
            score += 10
    return score
