package easy

import java.util.*
import kotlin.math.max

class Valid_Palindrome_125 {
    fun isPalindrome(s: String): Boolean { // 186 ms
//        val s = s.filter { it.isLetterOrDigit() }.toLowerCase() old version
        val s = s.filter { it.isLetterOrDigit() }.lowercase()
        val len = s.length
        if (len == 0) return true
        val end = max(0, (len / 2) - 1)
        for (i in 0..end) {
            if(s[i] != s[len - 1 -i]) return false
        }
        return true
    }

    fun isPalindromeWithNewString(s: String): Boolean {  // 2501 ms
        var res = ""
        for( c in s ) {
            if(c.isLetterOrDigit()) res += c.lowercase()
        }
        val len = res.length
        if (len == 0) return true
        val end = max(0, (len / 2) - 1)
        for (i in 0..end) {
            if(res[i] != res[len - 1 -i]) return false
        }
        return true
    }

    fun isPalindromeWithRegex(s: String): Boolean {  // 244 ms
        val s = Regex("[^a-z0-9]").replace(s.lowercase(Locale.getDefault()), "")
        return s == s.reversed()
    }
}

fun main(args: Array<String>) {
//    println(Valid_Palindrome_125().isPalindrome(""))
    println(Valid_Palindrome_125().isPalindromeWithRegex("A man, a plan, a canal: Panama"))
}
