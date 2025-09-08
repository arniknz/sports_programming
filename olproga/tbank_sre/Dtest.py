def visited_count(n, k):
    total_files = 2**n
    
    # Узлы дерева
    class Node:
        def __init__(self, left=None, right=None, file_id=None):
            self.left = left
            self.right = right
            self.file_id = file_id
    
    # Построение дерева
    def build(base, size):
        if size == 1:
            return Node(file_id=base)
        half = size // 2
        left = build(base, half)
        right = build(base + half, half)
        return Node(left, right)
    
    root = build(1, total_files)
    
    visited = 0
    direction = 0  # глобальный счётчик L/R
    stack = [(root, [])]  # стек: (узел, список уже посещённых детей)
    
    while stack:
        node, used = stack[-1]
        visited += 1  # каждый вход в узел считается
        
        if node.file_id is not None:
            if node.file_id == k:
                return visited
            stack.pop()
            continue
        
        choice = direction % 2
        direction += 1
        
        if choice == 0 and "L" not in used:
            stack[-1][1].append("L")
            stack.append((node.left, []))
        elif choice == 1 and "R" not in used:
            stack[-1][1].append("R")
            stack.append((node.right, []))
        else:
            if "L" not in used:
                stack[-1][1].append("L")
                stack.append((node.left, []))
            elif "R" not in used:
                stack[-1][1].append("R")
                stack.append((node.right, []))
            else:
                stack.pop()
    
    return visited

d, k = map(int, input().split())
print(visited_count(d, k))