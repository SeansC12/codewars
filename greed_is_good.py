def score(dice):
    print(dice)
    score = 0
    if dice.count(1) >= 3:
        score += 1000 + (dice.count(5) * 50) + ((dice.count(1) - 3) * 100)
    elif dice.count(6) >= 3:
        score += 600 + (dice.count(1) * 100) + (dice.count(5) * 50)
    elif dice.count(5) >= 3:
        score += 500 + (dice.count(1) * 100) + ((dice.count(5) - 3) * 50)
    elif dice.count(4) >= 3:
        score += 400 + (dice.count(1) * 100) + (dice.count(5) * 50)
    elif dice.count(3) >= 3:
        score += 300 + (dice.count(1) * 100) + (dice.count(5) * 50)
    elif dice.count(2) >= 3:
        score += 200 + (dice.count(1) * 100) + (dice.count(5) * 50)
    else:
        score += (dice.count(1) * 100) + (dice.count(5) * 50)
    return score