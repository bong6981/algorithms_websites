package botech.silver3

import java.util.StringTokenizer
import kotlin.math.max
import kotlin.math.min

class Q14888 {
}

fun main() {
    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()
    val nums = IntArray(n)
    run {
        val st = StringTokenizer(br.readLine())
        for(i in 0 until n) nums[i] = st.nextToken().toInt()
    }
    val operators = IntArray(4)
    run {
        val st = StringTokenizer(br.readLine())
        for(i in 0 until 4) operators[i] = st.nextToken().toInt()
    }

    var maxValue = Int.MIN_VALUE
    var minValue = Int.MAX_VALUE

    fun calculate(operand1: Int, opIdx: Int, operand2: Int) =
        when(opIdx) {
            0 -> operand1 + operand2
            1 -> operand1 - operand2
            2 -> operand1 * operand2
            // Kotlin/Java 정수 나눗셈은 0쪽으로 버림 → C++14 규칙과 동일
            3 -> operand1 / operand2
            else -> -1
        }

    fun dfs(idx: Int, value: Int) {
        if (idx == n) {
            maxValue = max(maxValue, value)
            minValue = min(minValue, value)
            return
        }

        for(opIdx in 0 until 4) {
            if(operators[opIdx] > 0) {
                operators[opIdx]--
                dfs(idx+1, calculate(value, opIdx, nums[idx]))
                operators[opIdx]++
            }
        }
    }

    dfs(1, nums[0])
    println(maxValue)
    println(minValue)
}

