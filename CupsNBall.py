def Ball():
    ball_location=1
    move=str.upper(input())#determine the location of ball
    for i in move:
        if i =="A":
            if ball_location ==1:
                ball_location+=1
            elif ball_location ==2:
                ball_location-=1
            else:
                ball_location+=0
        if i =="B":
            if ball_location ==1:
                ball_location+=0
            elif ball_location ==2:
                ball_location+=1
            else:
                ball_location-=1
        if i=="C":
            if ball_location==1:
                ball_location += 2
            elif ball_location==2:
                ball_location+=0
            else:
                ball_location-=2
    print(ball_location)
Ball()

