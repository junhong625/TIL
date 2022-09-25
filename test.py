def solution(commands):
    from collections import deque, defaultdict
    commands = deque(commands)
    excel = [[0 for _ in range(50)] for _ in range(50)]
    answer = []
    merge_list = defaultdict(list)

    while commands:
        com = commands.popleft().split()
        if com[0] == 'UPDATE':
            if len(com) == 4:
                r, c = map(int, com[1:3])
                if not excel[r][c][0]:
                    excel[r][c][1] = com[3]
                else:
                    while excel[r][c][0]:
                        r, c = excel[r][c][0]
                    excel[r][c][1] = com[3]
            else:
                for i in range(50):
                    for j in range(50):
                        if excel[i][j][1] == com[1]:
                            excel[i][j][1] = com[2]
        
        elif com[0] == 'MERGE':
            r1, c1, r2, c2 = map(int, com[1:])
            merge_list[(r1, c1)].append([r2, c2])
            merge_list[(r2, c2)].append([r1, c1])
            excel[r1][c1][2].extend([r2, c2])
            excel[r2][c2][0] = [r1, c1]    
        
        elif com[0] == 'UNMERGE':
            r, c = map(int, com[1:])
            if excel[r][c][0]:
                adjList = merge_list[tuple(excel[r][c][0])]
                while adjList:
                    dr, dc = adjList.pop()
                    if (dr,dc) != (r,c):
                        excel[dr][dc] = [False, 0, []]
                del merge_list[tuple(excel[r][c][0])]
            if excel[r][c][2]:
                for adj in excel[r][c][2]:
                    for adjList in merge_list[tuple(adj)]:
                        while adjList:
                            dr, dc = adjList.pop()
                            if (dr,dc) != (r,c):
                                excel[dr][dc] = [False, 0, []]
                        del merge_list[tuple(adj)]

            excel[r][c][0], excel[r][c][2] = False, []

        else:
            r, c = map(int, com[1:])
            while excel[r][c][0]:
                r, c = excel[r][c][0]
            answer.append(excel[r][c][1] if excel[r][c][1] else 'EMPTY')
    for r in excel:
        print(r)

    return answer

commands = list(map(str, input().replace('"', '').split(', ')))
# print(type(commands))
# for c in commands:
#     print(c)
print(solution(commands))