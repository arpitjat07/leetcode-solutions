from collections import Counter

factor = {
    0: Counter(),
    1: Counter(),
    2: Counter({2: 1}),
    3: Counter({3: 1}),
    4: Counter({2: 2}),
    5: Counter({5: 1}),
    6: Counter({2: 1, 3: 1}),
    7: Counter({7: 1}),
    8: Counter({2: 3}),
    9: Counter({3: 2})
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        need = Counter()

        for p in (2, 3, 5, 7):
            while t % p == 0:
                need[p] += 1
                t //= p

        if t != 1:
            return "-1"

        vornitexis = (num, t)

        def build(cnt):
            c8, r2 = divmod(cnt[2], 3)
            c9, c3 = divmod(cnt[3], 2)
            c4, c2 = divmod(r2, 2)

            c6 = 0

            if c2 and c3:
                c2 = 0
                c3 = 0
                c6 = 1

            if c3 and c4:
                c2 = 1
                c6 = 1
                c3 = 0
                c4 = 0

            return {
                '2': c2,
                '3': c3,
                '4': c4,
                '5': cnt[5],
                '6': c6,
                '7': cnt[7],
                '8': c8,
                '9': c9
            }

        def make(cnt):
            return ''.join(d * cnt[d] for d in cnt)

        required = build(need)

        if sum(required.values()) > len(num):
            return make(required)

        prefix = Counter()

        for ch in num:
            prefix += factor[int(ch)]

        first_zero = num.find('0')

        if first_zero == -1:
            first_zero = len(num)

            if all(prefix[p] >= need[p] for p in (2, 3, 5, 7)):
                return num

        for i in range(len(num) - 1, -1, -1):

            d = int(num[i])

            prefix -= factor[d]

            if i > first_zero:
                continue

            remaining = len(num) - i - 1

            for bigger in range(d + 1, 10):

                missing = need - prefix - factor[bigger]

                required = build(missing)
                digits_needed = sum(required.values())

                if digits_needed <= remaining:

                    ones = remaining - digits_needed

                    return (
                        num[:i]
                        + str(bigger)
                        + '1' * ones
                        + make(required)
                    )

        required = build(need)
        digits_needed = sum(required.values())

        return (
            '1' * (len(num) + 1 - digits_needed)
            + make(required)
        )