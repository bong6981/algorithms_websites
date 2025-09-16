package botech.silver3

class Q15652 {
}
fun main() {
    val br = System.`in`.bufferedReader()
    val (n, m) = br.readLine().split(" ").map { it.toInt() }

    val sb = StringBuilder()
    val sequence = IntArray(m)

    fun dfs(depth: Int, start: Int) {
        if(depth == m) {
            sb.append(sequence.joinToString(" ")).append("\n")
            return
        }

        for (i in start..n) {
            sequence[depth] = i
            dfs(depth + 1, i)
        }
    }

    dfs(0, 1)
    print(sb)
}
