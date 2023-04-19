package level1

// https://school.programmers.co.kr/learn/courses/30/lessons/76501?language=kotlin
class 음양더하기 {
    fun solution(absolutes: IntArray, signs: BooleanArray): Int {
        var answer: Int = 0
        for(idx in absolutes.indices) {
            if(signs[idx]) {
                answer += absolutes[idx]
            } else {
                answer -= absolutes[idx]
            }
        }
        return answer
    }

    fun other(absolutes: IntArray, signs: BooleanArray): Int =
        absolutes.foldIndexed(0) { index, acc, num ->  acc + if(signs[index]) num else -num }
}

/* 키워드
* indices
* foldIndexed
* */

/* foldIndexed
컬렉션의 모든 요소를 하나의 값으로 축소(reduce)하는 기능을 수행합니다.
foldIndexed 함수는 fold 함수와 유사하지만, 현재 처리 중인 요소의 인덱스를 함께 제공한다는 점이 다릅니다.
val numbers = listOf(1, 2, 3, 4, 5)
val sum = numbers.foldIndexed(0) { index, acc, number ->
    acc + number
}
println(sum) // 15 출력
 */

/*
def solution(absolutes, signs):
    answer = 0
    for x in range(len(absolutes)) :
        if(signs[x] == True) :
            answer += absolutes[x]
        else :
            answer -= absolutes[x]
    return answe
 */

