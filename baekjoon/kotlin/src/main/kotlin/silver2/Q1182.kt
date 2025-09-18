package silver2

import java.util.StringTokenizer

fun main() {
//   sol1()
   sol2()
}

/*
주의 : 공집합 빼야 함 (진 부분 수열)
 */
fun sol1() {
    val br = System.`in`.bufferedReader()
    val (n, s) = br.readLine().split(" ").map { it.toInt() }
    val numsSt = StringTokenizer(br.readLine())
    val nums = IntArray(n) { numsSt.nextToken().toInt() }

    var ans = 0

    for (i in 1 until (1 shl n)) {
        var acc = 0
        for (j in 0 until n) {
            if ((i and (1 shl j)) != 0) {
                acc += nums[j]
            }
        }
        if (acc == s) ans++
    }

    print(ans)
}


fun sol2() {
    val (n, s) = readLine()!!.split(" ").map { it.toInt() }
    val st = StringTokenizer(readLine())
    val nums = IntArray(n) { st.nextToken().toInt() }

    var ans = 0

    fun dfs(idx: Int, sum: Int) {
        if (idx == n) {
            if (sum == s) ans++
            return
        }

        dfs(idx+1, sum + nums[idx])
        dfs(idx+1, sum)
    }

    dfs(0, 0)

    if(s == 0) ans--
    print(ans)
}

