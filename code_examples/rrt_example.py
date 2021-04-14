def build(K=1000):
  tree = Tree()
  for k in range(K):
      rrt_extend(tree)
  return tree
  
def sample(tree):
    if rand() > α:
        return goal
    else:
        return uniform(x), uniform(y)
    