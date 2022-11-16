def points(games):
    points=[]
    for i in games:
        i = i.split(":")
        
        if int(i[0]) > int(i[1]):
            points.append(3)
            
        elif int(i[0])==int(i[1]):
            points.append(1)
        
    return sum(points)
