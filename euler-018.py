def treeDepth(node):
  depth = 0
  total = 0
  while total < node:
    depth += 1
    total += depth
  if total == node:
    return depth
  else:
    return depth - 1

def left(tree, node):
  return node + treeDepth(node) + 1

def right(tree, node):
  return node + treeDepth(node) + 2


treeString = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

t = map(int, treeString.strip().replace("\n", " ").split(" "))
maxAtNode = [-1] * len(t)

def getMaxPath(tree, startNode):
  if maxAtNode[startNode] >= 0:
    return maxAtNode[startNode]

  try:
    l = getMaxPath(tree, left(tree, startNode))
    r = getMaxPath(tree, right(tree, startNode))
  except IndexError:
    maxAtNode[startNode] = tree[startNode]
    return tree[startNode]

  maxAtNode[startNode] = tree[startNode] + max(l,r)
  return tree[startNode] + max(l,r)

print getMaxPath(t,0)