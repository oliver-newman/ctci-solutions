from graph import Graph
from collections import deque


def are_connected(graph, node1, node2):
    """
    Use bidirectional BFS to find if nodes are connected.
    """
    # TODO: this can be DRYed out quite a bit.

    queue1 = deque([node1])
    queue2 = deque([node2])

    visited1 = {node1}
    visited2 = {node2}

    while len(queue1) > 0 or len(queue2) > 0:
        if len(queue1) > 0:
            curr1 = queue1.pop()
            for neighbor1 in graph.out_neighbors(curr1):
                if neighbor1 not in visited1:
                    if neighbor1 in visited2:
                        return True
                    visited1.add(neighbor1)
                    queue1.appendleft(neighbor1)

        if len(queue2) > 0:
            curr2 = queue2.pop()
            for neighbor2 in graph.out_neighbors(curr2):
                if neighbor2 not in visited2:
                    if neighbor2 in visited1:
                        return True
                    visited2.add(neighbor2)
                    queue2.appendleft(neighbor2)

    return False


def test_are_connected():
    graph = Graph.random(n=100, p=0.05)
    for i in range(1, 100):
        graph.add_edge(i - 1, i)
    assert are_connected(graph, 0, 99)

