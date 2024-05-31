def main():
    n = int(input())
    scores = {}
    best = {
        "player": "",
        "score": -1
    }
    
    for _ in range(n):
        name, score = input().split()
        score = int(score)
        if name in scores:
            scores[name] += score
        else:
            scores[name] = score
            
        if scores[name] > best["score"]:
            best["player"] = name
            best["score"] = scores[name]

    print(best["player"])
            
main()