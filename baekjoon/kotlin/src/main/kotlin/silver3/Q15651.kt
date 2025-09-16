package botech.silver3

class Q15651 {
}

fun main() {
    val br = System.`in`.bufferedReader()
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val sb = StringBuilder()
    val sequence = IntArray(m)

    fun dfs(depth: Int) {
        if (depth == m) {
            sb.append(sequence.joinToString(" ")).append("\n")
            return
        }
        for (i in 1..n) {
            sequence[depth] = i
            dfs(depth + 1)
        }
    }

    dfs(0)
    print(sb)
}

