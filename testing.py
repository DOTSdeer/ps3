    count = 0
    word_count = hand.values()
    for amount in word_count:
        int(amount)
        if amount > 0:
            count +=1
            amount -=1
    return count 