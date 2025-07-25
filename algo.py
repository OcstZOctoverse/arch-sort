def arch_sort(list):
  greatest = True
  for i in range(1, len(list)):
    if list[0] <= list[i]:
        greatest = False
        break
    if greatest:
        for i in range(1, len(list)):
            temp = list[i]
            list[0] = list[i]
            list[i] = temp
  for i in range(len(list)):
    swap = False
    for j in range(i + 1, len(list)):
      if list[i] > list[j]:
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        swap = True
    if not swap:
      break #I don't know if this is the fastest way to do it, go this little swap thing from someone else
  return list
        
