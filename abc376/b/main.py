def isRightRound(move_positon, move_target_position, non_move_positon, end):
    flag = True
    distance = 0
    while distance < end:
        move_positon += 1
        distance += 1
        if move_positon % N == non_move_positon:
            flag = False
        if move_positon % N == move_target_position:
            break
    return flag,distance

L = 1
R = 2
total_distance = 0
N,Q= map(int, input().split())
for i in range(Q):
    A, B = input().split()
    B = int(B)
    move_position = L if A == "L" else R
    non_move_positon = R if A == "L" else L
    if move_position == B:
        continue
    isRight, distance = isRightRound(move_positon=move_position, move_target_position=B, non_move_positon=non_move_positon,end=N)
    if isRight:
        total_distance += distance
    else:
        total_distance += N - (B-move_position)
    
    if A == "L":
        L = B
    else:
        R = B 
print(total_distance)