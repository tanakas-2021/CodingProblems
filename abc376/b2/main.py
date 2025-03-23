def isRightRound(move_positon, move_target_position, non_move_positon, end):
    flag = True
    distance = 0
    while distance < end:
        move_positon += 1
        distance += 1
        if move_positon % end == non_move_positon % end:
            flag = False
        if move_positon % end == move_target_position % end:
            break
    return flag,distance

L = 1
R = 2
total_distance = 0
N,Q= map(int, input().split())
for i in range(Q):
    hand,hand_target_position  = input().split()
    hand_target_position = int(hand_target_position)
    hand_current_position = L if hand == "L" else R
    opponent_hand_current_position = R if hand == "L" else L 
    if hand_target_position == hand_current_position:
        continue
    isRight, distance = isRightRound(move_positon=hand_current_position, move_target_position=hand_target_position, non_move_positon=opponent_hand_current_position,end=N)
    if isRight:
        total_distance += distance
    else:
        total_distance += N - distance
    if hand == "L":
        L = hand_target_position
    else:
        R = hand_target_position 
print(total_distance)

    