package bong.sw.dp

class LIS

fun main() {
    println(lengthOfLIS(intArrayOf(2, 3, 6, 11, 13, 12)))
}

fun lengthOfLIS(nums: IntArray): Int {
    val c = mutableListOf<Int>()

    for (n in nums) {
        var left = 0
        var right = c.size

        while (left < right) {
            val mid = (left + right) / 2

            if (c[mid] < n) left = mid + 1
            else right = mid
        }

        if (left == c.size) c.add(n)
        else c[left] = n
    }

    return c.size
}
