package bong.sw.dp

class ShortestPath

const val INF = Int.MAX_VALUE / 2  // 오버플로 방지

fun printMatrix(matrix: Array<IntArray>) {
    for (row in matrix) {
        println(row.joinToString(" ") { if (it >= INF) "INF" else it.toString() })
    }
    println()
}

fun floydWarshallStepByStep(n: Int, dist: Array<IntArray>) {
    val result = Array(n) { i -> dist[i].clone() }

    println("초기 dist 배열:")
    printMatrix(result)

    for (k in 0 until n) {
        println("=== k = $k (중간 경유지 $k) ===")
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (result[i][k] != INF && result[k][j] != INF) {
                    val newDist = result[i][k] + result[k][j]
                    if (newDist < result[i][j]) {
                        println("dist[$i][$j] 갱신: ${result[i][j]} -> $newDist (경로: $i → $k → $j)")
                        result[i][j] = newDist
                    }
                }
            }
        }
        println("k=$k 후 dist 배열:")
        printMatrix(result)
    }

    println("최종 모든 정점 쌍 최단거리:")
    printMatrix(result)
}

fun main() {
//    val n = 4
//    val dist = arrayOf(
//        intArrayOf(0, 2, 5, INF),
//        intArrayOf(INF, 0, 1, 3),
//        intArrayOf(INF, INF, 0, 1),
//        intArrayOf(INF, INF, INF, 0)
//    )

    val n = 7
    val dist = arrayOf(
        intArrayOf(0, INF, 1, INF, INF, INF, INF),
        intArrayOf(INF, 0, INF, 1, INF, INF, INF),
        intArrayOf(INF, 1, 0, INF, INF, INF, INF),
        intArrayOf(INF, INF, INF, 0, INF, INF, 1),
        intArrayOf(INF, INF, INF, INF, 0, 1, INF),
        intArrayOf(INF, INF, INF, INF, INF, 0, INF),
        intArrayOf(INF, INF, INF, INF, 1, INF, 0),
    )

    floydWarshallStepByStep(n, dist)
}
