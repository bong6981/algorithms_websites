package easy

class MostCommonWord_819 {
    fun mostCommonWord(paragraph: String, banned: Array<String>): String {
        val wordsCountMap = mutableMapOf<String, Int>()

        paragraph
            .replace(Regex("[^a-zA-Z]"), " ")
            .split(" ")
            .filter { it.isNotBlank() }
            .map { it.lowercase() }
            .filter { it !in banned }
            .forEach {
                val count = wordsCountMap.getOrElse(it) { 0 }
                wordsCountMap[it] = count + 1
            }

        return wordsCountMap.maxByOrNull { it.value }!!.key
    }

}

fun main() {
    MostCommonWord_819().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", arrayOf("hit"))
}
