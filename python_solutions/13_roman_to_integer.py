class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        index = 0

        while index < len(s):
            print("Analysizing... " + str(s[index]))
            if s[index] == "I":
                if index + 1 >= len(s):
                    result += 1
                elif s[index + 1] == "V":
                    result += 4
                    index += 2
                    continue
                elif s[index + 1] == "X":
                    result += 9
                    index += 2
                    continue
                else:
                    result += 1
            elif s[index] == "X":
                if index + 1 >= len(s):
                    result += 10
                elif s[index + 1] == "L":
                    result += 40
                    index += 2
                    continue
                elif s[index + 1] == "C":
                    result += 90
                    index += 2
                    continue
                else:
                    result += 10
            elif s[index] == "C":
                if index + 1 >= len(s):
                    result += 100
                elif s[index + 1] == "D":
                    result += 400
                    index += 2
                    continue
                elif s[index + 1] == "M":
                    result += 900
                    index += 2
                    continue
                else:
                    result += 100
            elif s[index] == "V":
                result += 5
            elif s[index] == "L":
                result += 50
            elif s[index] == "D":
                result += 500
            else:
                result += 1000
            index += 1
        return result
        