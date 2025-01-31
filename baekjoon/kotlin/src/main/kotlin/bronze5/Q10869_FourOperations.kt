package botech.bronze5

import java.io.BufferedReader
import java.io.InputStreamReader

class Q10869_FourOperations

fun main(args: Array<String>) {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val input = br.readLine();
    val inputArray = input.split(" ")
    val a = inputArray[0].toInt()
    val b = inputArray[1].toInt()
//    val (a, b) = input.split(" ").map { it.toInt() } // 21276KB, 108ms

    println(a + b)
    println(a - b)
    println(a * b)
    println(a / b)
    println(a % b)

    br.close()
    // 14300KB 88ms
}
