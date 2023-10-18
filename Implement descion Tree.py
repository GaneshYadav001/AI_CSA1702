class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def build_decision_tree(X, y, depth=0, max_depth=None):
    # Check if we should stop splitting (e.g., reached max depth or all labels are the same)
    if depth == max_depth or len(set(y)) == 1:
        return TreeNode(data=max(set(y), key=y.count))

    num_features = len(X[0])
    best_split_feature, best_split_value, best_gini = None, None, 1.0

    # Iterate over each feature and its possible values to find the best split
    for feature in range(num_features):
        unique_values = set(X[i][feature] for i in range(len(X)))
        for value in unique_values:
            left_indices = [i for i in range(len(X)) if X[i][feature] == value]
            right_indices = [i for i in range(len(X)) if X[i][feature] != value]
            
            left_labels = [y[i] for i in left_indices]
            right_labels = [y[i] for i in right_indices]
            
            gini_left = 1.0 - sum((left_labels.count(label) / len(left_labels)) ** 2 for label in set(left_labels))
            gini_right = 1.0 - sum((right_labels.count(label) / len(right_labels)) ** 2 for label in set(right_labels))
            
            weighted_gini = (len(left_labels) / len(y)) * gini_left + (len(right_labels) / len(y)) * gini_right
            
            if weighted_gini < best_gini:
                best_gini = weighted_gini
                best_split_feature = feature
                best_split_value = value
                best_left_indices = left_indices
                best_right_indices = right_indices
    
    if best_gini == 1.0:
        return TreeNode(data=max(set(y), key=y.count))
    
    left_subtree = build_decision_tree([X[i] for i in best_left_indices], [y[i] for i in best_left_indices], depth+1, max_depth)
    right_subtree = build_decision_tree([X[i] for i in best_right_indices], [y[i] for i in best_right_indices], depth+1, max_depth)
    
    return TreeNode(data=(best_split_feature, best_split_value, left_subtree, right_subtree))

def predict(tree, x):
    if isinstance(tree.data, tuple):
        split_feature, split_value, left_subtree, right_subtree = tree.data
        if x[split_feature] == split_value:
            return predict(left_subtree, x)
        else:
            return predict(right_subtree, x)
    else:
        return tree.data

# Example usage:
X = [[0, 1], [1, 0], [1, 1], [0, 0]]
y = [0, 1, 1, 0]

tree = build_decision_tree(X, y, max_depth=1)
print(predict(tree, [1, 0]))  # Output: 1
