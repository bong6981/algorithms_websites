package botech.bronze2

class Q5618 {
}


fun main() {
    val br = System.`in`.bufferedReader()
    val n = br.readLine().toInt()
    val nums = br.readLine().split(" ").map { it.toInt() }

    tailrec fun gcd(a: Int, b: Int): Int = if(b == 0) a else gcd(b, a % b)

    var g = nums[0]
    for (i in 1 until n) g = gcd(g, nums[i])

    if (g == 1) {
        println(1)
        return
    }

    val small = ArrayList<Int>()
    val large = ArrayList<Int>()
    var i = 1
    while (i * i <= g) {
        if (g % i == 0) {
            small.add(i)
            val j = g / i
            if (i != j) large.add(j)
        }
        i++
    }

    val sb = StringBuilder()
    for (v in small) sb.appendLine(v)
    for (k in large.indices.reversed()) sb.appendLine(large[k])

    print(sb.toString())
}
