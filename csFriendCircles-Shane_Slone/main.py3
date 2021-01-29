def csFriendCircles(friendships):
    friend_circles = 0
    visited = set()
    def friend_checker(x, y):
        if not 0 <= x < len(friendships) or not 0 <= y < len(friendships[x]):
            return
        loc = f"{x}, {y}"
        cur = friendships[x][y]
        if cur == 0 or loc in visited:
            return
        else:
            visited.add(loc)
            friend_checker(x - 1, y)
            friend_checker(x + 1, y)
            friend_checker(x, y - 1)
            friend_checker(x, y + 1)       
    
    for i in range(len(friendships)):
        for j in range(len(friendships[i])):
            loc = f"{i}, {j}"
            if friendships[i][j] == 0:
                continue
            if loc not in visited:
                friend_circles += 1
                friend_checker(i, j)
    return friend_circles

