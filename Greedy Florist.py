if __name__ == '__main__':
    nest = []



    for _ in range(int(input())):
        name = input()
        score = float(input())
        a = [name,score]
        nest.append(a)

    nest.sort(key=lambda nest: nest[1])
    lowest = nest[0]
    second_lowest = []
    for i in range(1,len(nest)):
        if nest[i] == lowest:
            continue
        else:
            second_lowest = nest[i]
            break


    for i in range(1,len(nest)):
        if(nest[i]==second_lowest):
            second_lowest.append(nest[i])

    second_lowest.sort(key=lambda second_lowest: second_lowest[0])

    print(second_lowest)



