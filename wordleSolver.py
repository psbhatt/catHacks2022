import wordle
import pandas as pd
import random


def main():
    bank = pd.read_table('D:\PyCharm\catHacks\words.csv',header=None,names=['words'])
    bank = bank[bank['words'].str.len() == 5]
    final = bank.sample().iloc[0][0]
    # print(final)
    game = wordle.Wordle(word=final, real_words=True)
    print('adieu')
    response = game.send_guess('adieu')
    check = response[1]
    response = response[0].replace(" ", "")
    for i in range(5):
        if check:
            print("Algorithm was correct, answer was ", final)
            return True
        notin, used, corr = set(), {}, {}
        i = 0
        j = 0
        lc = 0
        while i < len(response):
            if response[i] == '*':
                corr[response[i + 1].lower()] = lc
                i += 2
            elif response[i].islower():
                notin.add(response[i].lower())
            else:
                used[response[i].lower()] = lc
            i += 1
            lc += 1

        for c in used:
            if c in notin :
                notin.remove(c)
        for c in corr:
            if c in notin :
                notin.remove(c)

        # print(notin, used, corr)

        for c in used:
            bank = bank[bank['words'].str.contains(c, na=False)].dropna()

        for c in used:
            bank = bank[bank['words'].str[used[c]] != c].dropna()

        for c in notin:
            bank = bank[bank['words'].str.contains(c, na=False) == False].dropna()

        for c in corr:
            bank = bank[bank['words'].str[corr[c]] == c].dropna()

        # print(bank['words'])
        response = '0'
        while len(response) < 5 and j < len(bank):
            response = game.send_guess(bank.iloc[j][0])
            if(isinstance(response,tuple)):
                check = response[1]
            response = response[0].replace(" ", "")
            bank = bank[bank['words'] != bank.iloc[j][0]]
            j += 1
        print(response.replace("*", "").lower())

    if check:
        print("Algorithm was correct, answer was ", final)
        return True
    else:
        print("Algorithm was not correct, correct answer was ", final)
        return False


if __name__ == '__main__':
    main()
