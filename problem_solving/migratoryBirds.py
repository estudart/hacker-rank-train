arr = [1, 1, 2, 2, 3]

def migratoryBirds(arr):
    max_rep = 0
    # Write your code here
    rep_id_dict = {}
    for bird_id in arr:
        if str(bird_id) not in rep_id_dict.keys():
            rep_id_dict[str(bird_id)] = 1
        else:
            rep_id_dict[str(bird_id)] += 1
    
    for key, value in rep_id_dict.items():
        if value > max_rep:
            max_rep = value

    rep_id_list = []
    for id, value in rep_id_dict.items():
        if value == max_rep:
            rep_id_list.append(id)

    return min(rep_id_list)

print(migratoryBirds(arr=arr))