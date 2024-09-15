#User function Template for python3
class Solution:
    def isSame(self, s):
        ln=len(s)
        count=0
        for i in s[::-1]:
            if i.isnumeric():
                count+=1
            else:
                break
        num=int(s[-count:])
        return int(num ==ln-count)
           
           
                
  


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)


# } Driver Code Ends