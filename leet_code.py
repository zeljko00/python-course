# def convert(s: str, numRows: int) -> str:
#     l = len(s)
#     result = ""
#     for row in range(numRows):
#         inc1 = 2 * row
#         inc2 = 2 * (numRows - (row + 1))
#         if inc1==0:
#             inc1=inc2
#         elif inc2==0:
#             inc2=inc1
#         index = row
#         inc = 0
#         while index < l:
#             result += s[index]
#             if inc % 2 == 1:
#                 index += inc1
#             else:
#                 index += inc2
#             inc += 1
#     return result


def convert(s: str, numRows: int) -> str:
        l = len(s)
        if l <= numRows or numRows == 1:
            return s
        else:
            result = [""] * l
            rows = [0] * numRows
            t = numRows * 2 - 2
            for index in range(l):
                mod = index % t
                if mod < numRows:
                    if mod > 0:
                        x = sum(rows[:mod])
                        print(x)
                        result[x + rows[mod]] = s[index]
                    else:
                        result[rows[mod]] = s[index]
                    rows[mod] += 1
                else:
                    x = sum(rows[:t - mod])
                    result[x + rows[t - mod]] = s[index]
                    rows[t - mod] += 1

            return str(result)

print(convert("PAYPALISHIRING",4))