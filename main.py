class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1 :
            return "1"
        if n == 2:
            return "11"
        char = "11"
        for i in range(3, n + 1):
            count = 1
            tmp = ""
            char += '$'
            length = len(char)
            for j in range(1, length):

                if char[j] != char[j - 1]:

                    tmp += str(count + 0)

                    tmp += char[j - 1]

                    count = 1
                else:
                    count += 1

            char = tmp
        return char
