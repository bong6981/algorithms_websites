package level0

class 문자열_겹쳐쓰기 {
    fun solution(myString: String, overwriteString: String, s: Int): String =
        myString.replaceRange(s, s + overwriteString.length, overwriteString )
}


fun main() {
    val result = 문자열_겹쳐쓰기().solution("He11oWor1d", "lloWorl", 2)
    println(result)
}
