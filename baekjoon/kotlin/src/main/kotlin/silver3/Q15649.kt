package botech.silver3

class Q15649 {
}

fun main() {
    val br = System.`in`.bufferedReader()
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val sb = StringBuilder()
    val sequence = IntArray(m)
    val visited = BooleanArray(n+1)

    fun dfs(depth: Int) {
        if (depth == m) {
            sb.append(sequence.joinToString(" ")).append("\n")
            return
        }
        for (i in 1..n) {
            if (visited[i].not()) {
                visited[i] = true
                sequence[depth] = i
                dfs(depth + 1)
                visited[i] = false
            }
        }
    }
    dfs(0)
    print(sb)
}
