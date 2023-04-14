package level1

// https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=kotlin
class 신고결과받기 {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
        var reporterMap = mutableMapOf<String, MutableSet<String>>()
        var userIdx = mutableMapOf<String, Int>()
        id_list.withIndex().forEach { (idx, user) -> userIdx[user] = idx }

        for(content in report) {
            val splitedContent = content.split(" ")
            val reporter = splitedContent[0]
            val reported = splitedContent[1]
            reporterMap.getOrPut(reported) { mutableSetOf() }.add(reporter)
        }

        var answer = IntArray(id_list.size)
        reporterMap.forEach{ report -> if(report.value.size >= k ) {
            for(reporter in report.value) {
                answer[userIdx[reporter]!!] += 1
            }
        }}
        return answer
    }

    fun other(id_list: Array<String>, report: Array<String>, k: Int): IntArray =
        report.map { it.split(" ") }
            .groupBy { it[1] }
            .asSequence()
            .map { it.value.distinct() }
            .filter { it.size >= k }
            .flatten()
            .map { it[0] }
            .groupingBy { it }
            .eachCount()
            .run { id_list.map { getOrDefault(it, 0) }.toIntArray() }
}

fun main(args: Array<String>) {
    println(신고결과받기().solution(
        arrayOf("muzi", "frodo", "apeach", "neo"),
        arrayOf("muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"),
        2
    ))
}
