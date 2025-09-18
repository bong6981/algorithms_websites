package botech.gold5

import java.math.BigInteger
import kotlin.math.pow

class Q1914 {
}


fun main() {
    val n = readLine()!!.toInt()
    val sb = StringBuilder()

    fun hanoi(n: Int, from: Int, to: Int, aux: Int, out: StringBuilder) {
        if (n == 0) {
            return
        }

        hanoi(n-1, from, aux, to, out)
        out.append(from).append(' ').append(to).append('\n')
        hanoi(n-1, aux, to, from, out)
    }

    // 일반 정수 shl 쓰면 문제 틀림. 이 문제는 N ≤ 100까지 들어오니, 이동 횟수 2의 n승 -1을 BigInteger로 계산해야 맞아요.
//    val count = BigInteger.ONE.shiftLeft(n).subtract(BigInteger.ONE)
    val count = BigInteger.TWO.pow(n).subtract(BigInteger.ONE)
    sb.append(count).append("\n")

    if (n <= 20) {
        hanoi(n, 1, 3, 2, sb)
    }

    print(sb.toString())
}
