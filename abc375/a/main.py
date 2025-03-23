def count_hashtag_dot_hashtag(s):
  count = 0
  for i in range(1,len(s) - 1):
    if s[i-1:i+2] == "#.#":
      count += 1
  return count

N = int(input())
s = input()
count = count_hashtag_dot_hashtag(s)
print(count) 