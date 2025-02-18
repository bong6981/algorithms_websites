package botech.bronze3

import java.io.BufferedReader
import java.io.InputStreamReader

class Multiply

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))
    val inputA = br.readLine()
    val inputB = br.readLine()

    val intA = inputA.toInt()
    val intB = inputB.toInt()

    println(intB % 10 * intA)
    println(intB % 100 / 10 * intA)
    println(intB / 100 * intA)
    println(intA * intB)
}
