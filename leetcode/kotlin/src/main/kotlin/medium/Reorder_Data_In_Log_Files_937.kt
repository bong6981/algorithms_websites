package medium

import java.util.StringJoiner

// https://leetcode.com/problems/reorder-data-in-log-files/
class Reorder_Data_In_Log_Files_937 {
    fun reorderLogFiles(logs: Array<String>): Array<String> {
        val letterLogs = mutableListOf<String>()
        val digitLogs = mutableListOf<String>()

        for(log in logs) {
            var arg = log.split(" ")[1]
            if(arg[0].isDigit()) digitLogs.add(log)
            else letterLogs.add(log)
        }

//        letterLogs.sortWith(
//            compareBy<String>{ it.substringAfter(" ")}
//                .thenBy { it.substringBefore(" ") }
//        )

        letterLogs.sortWith(compareBy({it.substring(it.indexOf(' ') + 1)}, {it.substring(0, it.indexOf(' '))}) )
        letterLogs.addAll(digitLogs)
        return letterLogs.toTypedArray()
    }
}

fun main(args: Array<String>) {
//    Reorder_Data_In_Log_Files_937().reorderLogFiles(arrayOf("a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"))
    println(reorderLogFiles(arrayOf("dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero")).toList())
}

fun reorderLogFiles(logs: Array<String>): Array<String> {
    val digits = mutableListOf<String>()
    val letterTriples = mutableListOf<Triple<Int, String, String>>()

    logs.forEachIndexed { idx, log ->
        val spaceIdx = log.indexOf(" ")

        if (log[spaceIdx+1].isDigit()) {
            digits.add(log)
        } else {
            val content = log.substring(spaceIdx + 1)
            val key = log.substring(0, spaceIdx)
            letterTriples.add(Triple(idx, key, content))
        }
    }

    letterTriples.sortWith(compareBy({it.third}, {it.second}))

    val letters = mutableListOf<String>()
    for (letterTriple in letterTriples) {
        letters.add(logs[letterTriple.first])
    }
    return (letters + digits).toTypedArray()
}

//fun reorderLogFiles(logs: Array<String>): Array<String> {
//    val letterLogs = mutableListOf<String>()
//    val digitLogs = mutableListOf<String>()
//
//    for(log in logs) {
//        var arg = log.split(" ")[1]
//        if(arg[0].isDigit()) digitLogs.add(log)
//        else letterLogs.add(log)
//    }
//
//    letterLogs.sortWith(
//        compareBy<String>{ it.substringAfter(" ")}
//            .thenBy { it.substringBefore(" ") }
//    )
//
//    letterLogs.addAll(digitLogs)
//    return letterLogs.toTypedArray()
//}
