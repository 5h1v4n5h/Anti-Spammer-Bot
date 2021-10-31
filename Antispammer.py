from collections import defaultdict


def spam_check(lst):
  restrict_message=[]
  d = defaultdict(int)
  for i in lst:
    d[i] += 1
  for i in d:
    if d[i]>10:
      restrict_message.append(i)
  return restrict_message