import numpy as np
class Node:
    def __init__(self,feature = None, threashod = None, left = None, right = None, *, value = None):
        self.feature = feature
        self.threashold = threashod
        self.left = left
        self.right = right
        self.value = value
        
    def is_leaf(self):
        return self.value is not None
    
class DecisionTree:
    #This helps prevent that the tree overgrows or overfits
    def __init__(self, max_depth):
         self.max_depth = max_depth
         self.root = None
         
    def fit(self, X, y):
        self.root = self._grow_tree(X,y)
        
        
    def _grow_tree(self,X ,y, depth = 0):
        num_samples, num_features = X.shape
        unique_labels = np.unique(y)
        
        if len(unique_labels) == 1 or (self.max_depth is not None and depth >= self.max_depth):
            return Node(value = Counter(y).most_common(1)[0][0])
        