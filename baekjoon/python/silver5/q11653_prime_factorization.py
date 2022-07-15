N = int(input())

if N != 1:
    while True:
        found = False
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                print(i)
                N //= i
                found = True
                break
        if not found:
            print(N)
            break


if N != 1:
    while True:
        found = False
        for i in range(2, int(N**0.5) + 1):
            if N % i == 0:
                print(i)
                N //= i
                found = True
                break
        if not found:
            print(N)
            break

        
        
def solution():
    #include<stdio.h>
# int main()
# {
# 	int n, i, j;
# 	scanf("%d",&n);
# 	for(i=2;i*i<=n;i++)
# 	{
# 		while(n%i==0)
# 		{
# 			n/=i;
# 			printf("%d\n",i);
# 		}
# 	}
# 	if(n>1)printf("%d\n",n);
# }



        

