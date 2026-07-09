'''
Experiment Title: Evaluating Pathfinding Efficiency using BFS and DFS
Objective
To analyze, simulate, and compare the behaviors of Breadth-First Search (BFS) and Depth-First Search (DFS) on a finite social network graph, understanding why traversal strategy impacts the discovery of the shortest path.
Problem Scenario
Imagine a localized social media network consisting of 6 individuals: Alice, Bob, Charlie, David, Emma, and Fred. The friendships (connections) between them are mutual and can be modeled as an undirected, unweighted graph.
The network connections are defined as follows:
•	Alice is connected to: Charlie, David
•	Charlie is connected to: Alice, Emma
•	David is connected to: Alice, Emma, Fred
•	Emma is connected to: Charlie, David, Bob
•	Fred is connected to: David, Bob
•	Bob is connected to: Emma, Fred

        [Charlie] --------- [Emma]
       /                                  |                \
  [Alice]                             |             [Bob]
       \                    	   |                /
          [David] ----------- [Fred]


Part A: Algorithm Simulation
Q1. Simulate the BFS Traversal  Assume Alice wants to find a connection path to Bob.
•	Trace the step-by-step execution of the Breadth-First Search (BFS) algorithm starting from Alice (Source) to find Bob (Goal).
•	Show the state of the Queue and the list of Visited nodes at each step.
•	Final Path Found by BFS: Alice -> Charlie -> Emma -> Bob


Q2. Simulate the DFS Traversal  Assume Alice wants to find a connection path to Bob.
•	Trace the step-by-step execution of the Depth-First Search (DFS) algorithm starting from Alice (Source) to find Bob (Goal). (Remember to push/visit neighbors in alphabetical order).
•	Show the state of the Stack and the list of Visited nodes at each step.
•	Final Path Found by DFS: Alice -> Charlie -> Emma -> Bob
Part B : Code implementation
Write a complete Python implementation to simulate both BFS and DFS on the specified social network graph


'''

from collections import deque

def bfs(graph, start, goal):
    print(f"\n--- BFS Traversal ({start} -> {goal}) ---")
    queue = deque([[start]])
    visited = []
    
    step = 1
    while queue:
        queue_state = [path[-1] for path in queue]
        print(f"Step {step}:")
        print(f"  Queue: {queue_state}")
        print(f"  Visited: {visited}")
        
        path = queue.popleft()
        node = path[-1]
        
        if node == goal:
            print(f"Goal '{goal}' reached!")
            print(f"  Final Path Found by BFS: {' -> '.join(path)}")
            return path
            
        if node not in visited:
            visited.append(node)
            for neighbor in sorted(graph.get(node, [])):
                if neighbor not in visited:
                    queue.append(path + [neighbor])
        step += 1

def dfs(graph, start, goal):
    print(f"\n--- DFS Traversal ({start} -> {goal}) ---")
    stack = [[start]]
    visited = []
    
    step = 1
    while stack:
        stack_state = [path[-1] for path in stack]
        print(f"Step {step}:")
        print(f"  Stack: {stack_state}")
        print(f"  Visited: {visited}")
        
        path = stack.pop()
        node = path[-1]
        
        if node == goal:
            print(f"Goal '{goal}' reached!")
            print(f"  Final Path Found by DFS: {' -> '.join(path)}")
            return path
            
        if node not in visited:
            visited.append(node)
            # Push in reverse alphabetical order so that alphabetical first is popped next
            for neighbor in sorted(graph.get(node, []), reverse=True):
                if neighbor not in visited:
                    stack.append(path + [neighbor])
        step += 1

if __name__ == "__main__":
    social_network = {
        'Alice': ['Charlie', 'David'],
        'Bob': ['Emma', 'Fred'],
        'Charlie': ['Alice', 'Emma'],
        'David': ['Alice', 'Emma', 'Fred'],
        'Emma': ['Bob', 'Charlie', 'David'],
        'Fred': ['Bob', 'David']
    }
    
    bfs(social_network, 'Alice', 'Bob')
    dfs(social_network, 'Alice', 'Bob')