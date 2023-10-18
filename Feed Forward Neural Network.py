def relu(n):
    return max(0, n)
def dot_product(input_data, weights):
    return sum(x * w for x, w in zip(input_data, weights))
def feedforward(input_data, weights):
    node0 = relu(dot_product(input_data, weights[0]))
    node1 = relu(dot_product(input_data, weights[1]))
    node2 = relu(dot_product([node0, node1], weights[2]))
    node3 = relu(dot_product([node0, node1], weights[3]))
    output = relu(dot_product([node2, node3], weights[4]))
    return output
inp = [[-1, 2], [2, 2], [3, 3]]
weights = [[3, 3], [1, 5], [3, 3], [1, 5], [2, -1]]
for x in inp:
    output = feedforward(x, weights)
    print(f"Input: {x}, Output: {output}")
