#Code for Breath First Search Algorithm
def bfs(visited,graph,node):
  visited.append(node)
  queue.append(node)
  while queue:
    m=queue.pop(0)
    print(m,end=" ")
    for neighbor in graph[m]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)
graphs={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited=[]
queue=[]
#Calling a function
bfs(visited,graphs,node)
