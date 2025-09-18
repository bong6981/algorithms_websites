package level1

class 최대공약수와최소공배수 {
    fun solution(n: Int, m: Int): IntArray {

        fun gcd(a: Int, b: Int): Int =
            if (b == 0) a else gcd(b, a %b)

        val gcdValue = gcd(n, m)
        val lcmValue = n * m / gcdValue

        return intArrayOf(gcdValue, lcmValue)
    }
}
