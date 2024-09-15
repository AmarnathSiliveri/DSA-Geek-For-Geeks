#User function Template for python3

class Solution:

    def isGoodString(self, s):
        # code here
        for i in range(len(s)-1):
            if not ((s[i] =='a' and s[i+1] =="z") or (s[i] =='z' and s[i+1]=='a')):
                if abs(ord(s[i])-ord(s[i+1])) == 1:
                    continue
                else:
                    return 'NO'
        return "YES"
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.isGoodString(s)

        print(ans)
# } Driver Code Ends