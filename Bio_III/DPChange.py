# Works

"""
Given a quantity of money and a list of coins, return the minimum number of coins.
"""
def DPChange(money, coins):
    MinNumCoins = [0]*(money+1)
    MinNumCoins[0] = 0
    for m in range(1, money+1): 
        MinNumCoins[m] = 100000
        for i in range(0, len(coins)):
            if m >= coins[i]:  # only take coins not greater than money
                if MinNumCoins[m-coins[i]] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m-coins[i]] + 1
    return MinNumCoins[money]


def test():
    in_ = (40, [50,25,20,10,5,1])
    out_ = 2
    assert(DPChange(*in_) == out_), "Test 1 FAILED"

    in_ = (8074, [24,13,12,7,5,3,1])
    out_ = 338
    assert(DPChange(*in_) == out_), "Test 2 FAILED"


if __name__ == "__main__":
    money = 16807
    coins = [18,17,16,7,6,5,3,1]
    print(DPChange(money, coins))


