package level1

import java.util.StringJoiner

class 개인정보수집유효기간 {
    fun solution(today: String, terms: Array<String>, privacies: Array<String>): IntArray {
        var answer = mutableListOf<Int>()

        val today_to_day = toDay(today.split("."))
        val kind_terms_day = mutableMapOf<String, Int>()
        terms.forEach {
            val (kind, m) = it.split(" ")
            kind_terms_day[kind] = m.toInt() * 28
        }

        for (idx in privacies.indices) {
            val privacy = privacies[idx]
            val (date, kind) = privacy.split(" ")
            if(toDay(date.split(".")) + kind_terms_day[kind]!! <= today_to_day) {
                answer.add(idx+1)
            }
        }


        return answer.toIntArray()
    }

    fun toDay(date: List<String>): Int =
        date[0].toInt() * 12 * 28 + (date[1].toInt() - 1) * 28 + date[2].toInt()
}

/* python - sol()
def solution(today, terms, privacies):
    answer = []
    today = today.split(".")
    this_y = int(today[0])
    this_m = int(today[1])
    this_d = int(today[2])

    terms_dic = {}

    for term in terms:
        kind, month = term.split(" ")
        terms_dic[kind] = int(month) * 28

    for idx, privacy in enumerate(privacies):
        date, kind = privacy.split()
        y, m, d = date.split(".")
        day = (this_y - int(y)) * 28 * 12 + (this_m - int(m)) * 28 + (this_d - int(d)) + 1
        if terms_dic[kind] >= day  : continue
        else : answer.append(idx+1)

    return answer
 */
/* python - other()
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = { v[0] : int(v[2:]) for v in terms}
    today = to_days(today)

    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
 */
