'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.'''


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    winner = -1000
    runner_up = -1000

    for i in range(0, n):
        a = arr[i]
        if (a > winner):
            runner_up = winner
            winner = a
        elif (a < winner and a >= runner_up):

            runner_up = a

    print(runner_up)
