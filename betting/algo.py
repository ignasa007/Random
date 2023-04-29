class Node:

    def __init__(self, value=None, result='', parent=None):
        self.value = value 
        self.result = result 
        self.parent = parent 
        self.left_child = None
        self.right_child = None
    
    def add_children(self, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child
    
    def get_children(self):
        return self.left_child, self.right_child


def make_graph(root, depth):

    nodes_at_next_level = [root]

    while nodes_at_next_level:

        nodes_at_level, nodes_at_next_level = nodes_at_next_level, []
        for node in nodes_at_level:

            if node.result.count('A') == (depth+1)//2 or node.result.count('B') == (depth+1)//2:
                continue

            left_child, right_child = Node(result=node.result+'A', parent=node), Node(result=node.result+'B', parent=node)
            for child in (left_child, right_child):

                if child.result.count('A') == (depth+1)//2:
                    child.value = 100
                elif child.result.count('B') == (depth+1)//2:
                    child.value = -100
                nodes_at_next_level.append(child)

            node.add_children(left_child, right_child)

    return nodes_at_level


def populate_values(nodes_at_level, depth):

    for _ in range(depth):
    
        nodes_at_prev_level = []
        for child in nodes_at_level:
            if child.parent.value is not None:
                continue
            parent = child.parent
            left_child, right_child = parent.left_child, parent.right_child
            parent.value = (left_child.value+right_child.value)/2
            nodes_at_prev_level.append(parent)
        nodes_at_level = nodes_at_prev_level

    
def print_tree(root, attr='value'):

    nodes_at_level = [root]
    while nodes_at_level:
        print(*(node.value if attr == 'value' else node.result for node in nodes_at_level))
        nodes_at_level = [child for node in nodes_at_level for child in node.get_children() if child is not None]


def bets(root, depth):

    nodes_at_level = [root]
    for _ in range(depth):
        print(*(node.get_children()[0].value-node.value for node in nodes_at_level if node.get_children()[0]))
        nodes_at_level = [child for node in nodes_at_level for child in node.get_children() if child is not None]


def main(depth):

    root = Node(result='', parent=None)
    leaves = make_graph(root, depth) 

    root.result = 'O'
    print('\nTree nodes\n')
    print_tree(root, 'result')

    print('\nValue at each node\n')
    populate_values(leaves, depth)
    print_tree(root, 'value')
    
    print('\nBet at each node\n')
    bets(root, depth)


if __name__ == '__main__':

    depth = input('How many games are being played? ')
    while not depth.isnumeric() or int(depth) <= 0:
        print('Please enter an integer greater than 0.')
        depth = input('How many games are being played? ')
    depth = int(depth)

    main(depth)
