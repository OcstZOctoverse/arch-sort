def arch_sort(list):
  for i in range(len(list)):
    swap = False
    for item in list:
      if item > list[i]:
        temp = list[list.index(item)]
        list[list.index(item)] = list[i]
        list[i] = temp
        swap = True
    if not swap:
      break #I don't know if this is the fastest way to do it, go this little swap thing from someone else
  return list
        
