class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        ones = num % 10
        tens = num % 100 // 10
        hundreds = num % 1000 // 100
        thousands = num % 10000 // 1000

        # THOUSANDS PLACE
        for _ in range(thousands):
            result += "M"
        
        # HUNDREDS PLACE
        if hundreds == 9:
            result += "CM"
        elif hundreds > 4:
            result += "D"
            for _ in range(5, hundreds):
                result += "C"
        elif hundreds == 4:
            result += "CD"
        else:
            for _ in range(hundreds):
                result += "C"

        # TENS PLACE
        if tens == 9:
            result += "XC"
        elif tens > 4:
            result += "L"
            for _ in range(5, tens):
                result += "X"
        elif tens == 4:
            result += "XL"
        else:
            for _ in range(tens):
                result += "X"

        # ONES PLACE
        if ones == 9:
            result += "IX"
        elif ones > 4:
            result += "V"
            for _ in range(5, ones):
                result += "I"
        elif ones == 4:
            result += "IV"
        else:
            for _ in range(ones):
                result += "I"

        return result