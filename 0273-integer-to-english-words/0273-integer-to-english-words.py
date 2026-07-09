class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six",
            "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def helper(n):
            if n == 0:
                return ""
            if n < 20:
                return below20[n] + " "
            if n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            return (
                below20[n // 100]
                + " Hundred "
                + helper(n % 100)
            )

        res = ""

        billions = num // 1000000000
        if billions:
            res += helper(billions) + "Billion "
        num %= 1000000000

        millions = num // 1000000
        if millions:
            res += helper(millions) + "Million "
        num %= 1000000

        thousands = num // 1000
        if thousands:
            res += helper(thousands) + "Thousand "
        num %= 1000

        if num:
            res += helper(num)

        return res.strip()