T = int(input())

for i in range(T):
    N = int(input())
    beauty_scores = list(map(int,[x for x in input().strip()]))
    B = max(beauty_scores)
    B_index = beauty_scores.index(B)
    if B_index!=len(beauty_scores):
        B_left = beauty_scores[B_index-1]
    if B_index != len(beauty_scores):
        B_right = beauty_scores[B_index+1]
    
    painted = []
    first_remove = []
    # paint towards:
    if B_right>B_left:
        towards = 'right'
        first_remove = beauty_scores[:B_index]
    if B_left>B_right:
        towards = 'left'
        first_remove = beauty_scores[B_index:]

    duplicates_present = False
    if len(first_remove) == len(beauty_scores):
        duplicates_present = True
    # painting begins
    # for x in range(0,N):
    x = 0
    while x<len(beauty_scores):
        if towards=='right':
            try:
                score = beauty_scores[B_index+x]
                painted.append(score)
                if len(first_remove)!=0:
                    first_remove.remove(first_remove[0])
                else:
                    beauty_scores.remove(beauty_scores[-1])
            except Exception as identifier:
                pass

        if towards=='left':
            try:
                score = beauty_scores[B_index+x]
                painted.append(score)
                if len(first_remove)!=0:
                    first_remove.remove(first_remove[0])
                else:
                    beauty_scores.remove(beauty_scores[1])
            except Exception as identifier:
                pass
        x+=1
        if duplicates_present and (len(beauty_scores)<=1 or len(first_remove)<=1):
            break
    total_score = sum(painted)
    print('Case #{}: {}'.format(i+1,total_score))