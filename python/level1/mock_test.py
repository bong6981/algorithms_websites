def solution(answers):
    correct = [0, 0, 0]
    first_p = [1, 2, 3, 4, 5]
    second_p = [2, 1, 2, 3, 2, 4, 2, 5]
    third_p = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer_list = []

    for i in range(len(answers)):
        if answers[i] == first_p[i%5] :
            correct[0] += 1
        if answers[i] == second_p[i%8] :
            correct[1] += 1
        if answers[i] == third_p[i%10] :
            correct[2] += 1
        
    max_answer = max(correct)
    for i in range(3) :
        if max_answer == correct[i]:
            answer_list.append(i+1)
    
    return answer_list


answers = [1,2,3,4,5]
print(solution(answers))