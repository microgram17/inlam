def divecalculator():
    judge_amnt = int(input("Hur många domare finns?: "))
    if judge_amnt <=2:
        print("less than 3")
    else:
        diff_grade = int(input("Svårighetsgrad på hopp?: "))
        judge_points = [
            int(input(f"Hur många poäng ger domare #{str(_ + 1)}: "))
            for _ in range(judge_amnt)
        ]
    judge_points.remove(min(judge_points))
    judge_points.remove(max(judge_points))
    total_points = sum(judge_points)
    average_points = total_points / (len(judge_points))
    final_score = average_points * 3 * diff_grade
    print(f"Hoppet fick: {final_score} poäng!")

jump_amnt = int(input("Hur många hopp ska dömmas?: "))
for _ in range(jump_amnt):
    print(f"Hopp #{str(_+1)}:")
    divecalculator()