import sys

def get_table(path):
    with open(path, 'r') as f:
        return [[int(num) for num in line.split()] for line in f]

def start_positions(table):
    return [[i, j] for i in range(len(table)) for j in range(len(table[0])) if table[i][j] == 1]

def is_goal_state(table, row, col):
    return table[row][col] == 3

def is_valid_move(table, row, col):
    return 0 <= row < len(table) and 0 <= col < len(table[0]) and (table[row][col] == 3 or table[row][col] == 2)

def get_neighbours(table, pos):
    return [[pos[0] + dr, pos[1] + dc] for dr, dc in [(0, -1), (1, 0), (0, 1), (-1, 0)] if is_valid_move(table, pos[0] + dr, pos[1] + dc)]

def bfs(table, musk_pos):
    queue = [(musk_pos, [musk_pos])]
    visited, search_queue = [], []
    
    while queue:
        pos, path = queue.pop(0)
        visited.append(pos)
        
        if is_goal_state(table, pos[0], pos[1]):
            search_queue.append(search_queue[-1][1:])
            return visited, search_queue, path
        
        frontier = search_queue[-1][1:] if len(search_queue) else []
            
        for neighbour in get_neighbours(table, pos):
            if neighbour not in visited and neighbour not in frontier:
                queue.append((neighbour, path + [neighbour]))
                frontier.append(neighbour)
            
        search_queue.append(frontier)
        
    return None

def dfs(table, musk_pos):
    stack = [(musk_pos, [musk_pos])]
    visited, search_queue = [], []
    
    while stack:
        pos, path = stack.pop()
        visited.append(pos)
        
        if is_goal_state(table, pos[0], pos[1]):
            search_queue.append(search_queue[-1][:-1])
            return visited, search_queue, path
        
        frontier = search_queue[-1][:-1] if len(search_queue) else []
            
        for neighbour in get_neighbours(table, pos):
            if neighbour not in visited and neighbour not in frontier:
                stack.append((neighbour, path + [neighbour]))
                frontier.append(neighbour)
            
        search_queue.append(frontier)
        
    return None

def main():
    params = sys.argv

    if len(params) == 3:
        path_len = float('inf')
        file_path, search_type = params[1], int(params[2])
        table = get_table(file_path)
        musk_positions = start_positions(table)
        explored, search, path = 0, 0, 0
        for musk_pos in musk_positions:
            paths = bfs(table, musk_pos) if search_type == 0 else dfs(table, musk_pos)
            if paths and len(paths[2]) < path_len:
                explored, search, path = paths
                path_len = len(paths[2])
        print('exploredNodes =', explored)
        print('searchQueue = [', *search, ']',sep='\n')
        print('shortestPath =', path)

if __name__ == "__main__":
    main()
