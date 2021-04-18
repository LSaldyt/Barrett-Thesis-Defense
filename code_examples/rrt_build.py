def build(K=1000): 
  step = 50    # evolved
  rewire = 100 # evolved
  tree = Tree() # const
  for k in range(K):
      p = sample(tree)
      tree.extend(p)
  return tree
  