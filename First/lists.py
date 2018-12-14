friends = ['Ravi', 'Loki', 'Naveen', 'Hussain', 'Hareesh', 'vinod', 'ajay']
print(friends)
print(len(friends))
print(friends[len(friends)-1])
print(friends[0:-1])
print(friends[:len(friends)])
print(friends[round((len(friends))/2):])
print(friends[:round((len(friends))/2)])

#append - used to append data at the end of list
friends.append('adarsh')

print(friends)
#insert - insert new data in between list

friends.insert(round((len(friends))/2), 'jagan')
print(friends)

insiders = ['gamya', 'thirupal', 'charan']
#extend - used to add one list data to another list....append - to add data....extend - to add lists

friends.extend(insiders)
#"remove" - to remove specific data from list
#"pop" - to remove last indexed data in list....popped-pop() object

friends.remove('ajay')
popped = friends.pop()

print(popped)
print(friends)

#"reverse" - te reverse whole list
#"sort()" , "sorted" - sort list elements in alphabetical order
#list.sort(reverse=true) - reverse the elements from last to first in sorted

friends.reverse()
print(friends)
friends.sort()
print(friends)

friends.sort(reverse=True)
intermediates = sorted(friends)
print(intermediates)

num = [10, 30, 25, 87, 12]
print(min(num))
print(max(num))
print(sum(num))

print(intermediates.index('Ravi'))

l = 25 not in num
print(l)













