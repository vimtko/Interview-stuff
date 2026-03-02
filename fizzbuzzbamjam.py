#Codetraining
#3/2/2026

#make a print of 100 but print when:
# fizz when is %3
# buzz when is %5
# fizzbuzz when its %3 and %5
# bam when its %7
# jam when its %10

for i in range(101):
    # fizzbuzz when its %3 and %5
    if i %3==0 and i%5==0:
        print(f'{i} fizzbuzz')
     # fizz when is %3
    if i %3==0 :
        print(f'{i} fizz')
    # buzz when is %5 
    if i% 5==0:
        print(f'{i} buzz')
    # jam when its %10
    if i %10==0 :
        print(f'{i} bam')
    # bam when its %7
    if i %7==0 :
        print(f'{i} jam')
