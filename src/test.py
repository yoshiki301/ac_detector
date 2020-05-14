import fetch_submission
if __name__ == '__main__':
    memo = fetch_submission.fetch_ac_count()
    string = ""
    for user in memo:
        string += user+":" + str(memo[user]) + "\n"
    print(string)
