from collections import deque
def solution(cacheSize, cities):
    cache=deque([])
    answer = 0
    for i in range(len(cities)):
        if cacheSize==0:
            answer=5*len(cities)
            return answer
        if cities[i].upper() in cache:
            answer+=1
            cache.remove(cities[i].upper())
            cache.append(cities[i].upper())
        else:
            if cacheSize==len(cache):
                answer+=5
                cache.popleft()
                cache.append(cities[i].upper())
            else:
                answer+=5
                cache.append(cities[i].upper())
    
    return answer