class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x=0
        result=""
        for i in range(-1,-(min(len(a),len(b))+1),-1):
            sum=int(a[i])+int(b[i])+x
            if sum>=2:
                result=str(sum-2)+result
                x=sum//2
            else:
                result=str(sum)+result
                x=0
        if(len(a)>len(b)):
            for j in range(i-1,-(len(a)+1),-1):
                sum = int(a[j]) + x
                if sum >= 2:
                    result = str(sum - 2) + result
                    x = sum // 2
                else:
                    result = str(sum) + result
                    x = 0
        elif(len(b)>len(a)):
            for j in range(i-1, -(len(b) + 1),-1):
                sum = int(b[j]) + x
                if sum >= 2:
                    result = str(sum - 2) + result
                    x = sum // 2
                else:
                    result = str(sum) + result
                    x = 0
        if x==1:
            result="1"+result

        return result

sol=Solution()
print(sol.addBinary("1","111"))