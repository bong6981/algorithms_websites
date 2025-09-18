package botech.gold4

class Q9663 {
}

fun main() {
//    sol1()
    sol2()
}

fun sol2() {
    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()

    val fullMask = (1 shl n) - 1
    var ans = 0

    fun dfs(columns: Int, diag1: Int, diag2: Int) {
        if (columns == fullMask) {
            ans++
            return
        }

        var available = fullMask and (columns or diag1 or diag2).inv()

        while(available != 0) {
            val bit = available and -available
            available -= bit

            val nextColumns = columns or bit
            val nextdiag1 = ((diag1 or bit) shl 1) and fullMask
            val nextdiag2 = (diag2 or bit) ushr 1

            dfs(nextColumns, nextdiag1, nextdiag2)
        }
    }

    dfs(0, 0, 0)
    print(ans)
}

fun sol1() {
    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()

    val col = IntArray(n)
    var ans = 0

    fun attackable(r1: Int, c1: Int, r2: Int, c2: Int) =
        when {
            c1 == c2 -> true
            r1 - c1 == r2 - c2 -> true
            r1 + c1 == r2 + c2 -> true
            else -> false
        }

    fun dfs(row: Int) {
        if (row == n) {
            ans++
            return
        }

        for (c in 0 until n) {
            var possible = true

            for (j in 0 until row) {
                if (attackable(row, c, j, col[j])) {
                    possible = false
                    break
                }
            }

            if (possible) {
                col[row] = c
                dfs(row + 1)
                col[row] = 0
            }
        }
    }

    dfs(0)
    println(ans)
}

