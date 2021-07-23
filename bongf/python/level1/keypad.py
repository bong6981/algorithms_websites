def solution(numbers, hand):
    answer = ''
    location = [ [3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2] ]
    left = [3, 0]
    right = [3, 2]
    for number in numbers :
        if number in (1, 4, 7) :
            answer += 'L'
            left = location[number]
            
        elif number in (3, 6, 9) :
            answer += 'R'
            right = location[number]

        else :
            x, y = location[number]
            left_distance = abs(x-left[0]) + abs(y-left[1])
            right_distance = abs(x-right[0]) + abs(y-right[1])

            if left_distance < right_distance :
                left = location[number]
                answer += 'L'
            elif left_distance > right_distance :
                right = location[number]
                answer += 'R'
            else :
                if hand == 'right' :
                    right = location[number]
                    answer += 'R'
                else :
                    left = location[number]
                    answer += 'L'
                        
    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))