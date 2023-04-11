package level1

class 나머지가1이되는수 {
    fun solution(n: Int): Int {
        val target = n - 1
        var answer: Int = 0

        for(i in 2..target) {
            if(target % i == 0) {
                answer = i
                break
            }
        }

        return answer
    }

    fun other(n: Int): Int = (1..n).first{ n % it == 1}

}
