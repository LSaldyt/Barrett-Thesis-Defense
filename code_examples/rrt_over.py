# Default RRT*
def rrt_star(start, end):
  K = 1000 # Num nodes
  tree = Tree()
  for k in range(K): 
      # Uniformly sample 
      p = sample(bias, end)
      # Add them to tree
      tree.extend(p, step)
      # Rewire nearby paths
      tree.rewire(p, rad)
  return tree
  