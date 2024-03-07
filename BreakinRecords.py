scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]


def breakingRecords(scores):
    # Write your code here
    mini = scores[0]
    maxi = scores[0]

    mini_count = 0
    maxi_count = 0

    for score in scores[1:]:
        if score > maxi:
            maxi = score
            maxi_count+=1
        elif score < mini:
            mini = score
            mini_count+=1

    return [maxi_count, mini_count]

print(breakingRecords(scores))