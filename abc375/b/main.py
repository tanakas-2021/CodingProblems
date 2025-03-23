def get_distace(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)**0.5

total_distance = 0
current_x, current_y = 0,0
n = int(input())
for _ in range(n):
    target_x,target_y = map(int, input().split())
    total_distance += get_distace(current_x,current_y,target_x,target_y)
    current_x = target_x
    current_y = target_y
total_distance += get_distace(current_x,current_y,0,0)
print(total_distance)