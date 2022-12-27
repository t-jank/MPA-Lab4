# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:25:20 2022

@author: t-jan
"""
import random
import math
import matplotlib.pyplot as plt
import statistics


def random_permutation(n):
    a=[]
    for i in range(0,n): a.append(i+1)
    for i in range(0,n-1): # Fisher–Yates shuffle
        j = random.randint(i,n-1)
        a[i], a[j] = a[j], a[i]
    return a

def fixed_points(permutation):
    n=len(permutation)
    fixed_points_counter=0
    for i in range(0,n):
        if permutation[i]==i+1:
            fixed_points_counter+=1
    return fixed_points_counter

def records(permutation):
    n=len(permutation)
    records_counter=0
    for i in range(0,n-1):
        if permutation[i+1]>permutation[i]:
            records_counter+=1
    return records_counter

def cycles(permutation):
    n=len(permutation)
    '''
    expected_cycles_1 = 0
    for i in range(1,n+1): expected_cycles_1+=(1/i)
    gamma=0.57721566490153286
    expected_cycles_2=math.log1p(n)+gamma
    '''
    flags=[]
    for i in range(0,n): flags.append('n')
    cycles_counter=0
    for i in range(0,n):
        index=i
        if flags[i]=='n':
            cycles_counter+=1
            while flags[index]!='t':
                flags[index]='t'
                value=permutation[index]
                index=value-1
    return cycles_counter

nMin=5
nMax=1000
nStep=1
nRepeats=1
alfa=0.1 #0.1=90%
#fp_big_sum=0
draw=True
results=[]

for n in range(nMin,nMax,nStep):
    summ=0
    for r in range(0,nRepeats): 
        a = random_permutation(n)
        fp = fixed_points(a)
     #   cc = cycles(a)
     #   rc=records(a)
        results.append(fp)
        summ += fp
     #   fp_big_sum += fp
    if draw==True:
        plt.scatter(n,summ/nRepeats,color='k')
if draw==True:
    plt.xlim(left=0)
    plt.xlim(right=nMax)
    plt.xlabel('n')
    plt.ylabel('fixed points')
    plt.title('Liczba punktów stałych losowej permutacji')
#print('Average number of fixed points:',fp_big_sum/(math.ceil((nMax-nMin)/nStep)*nRepeats))
deltaczeb=math.sqrt(statistics.variance(results)/alfa)
avgres=statistics.mean(results)
yczeb1=2*[avgres+deltaczeb]
yczeb2=2*[avgres-deltaczeb]
xrange=[nMin,nMax-1]
plt.plot(xrange,yczeb1,color='b',label='Czebyszew, α='+str(1-alfa))
plt.plot(xrange,yczeb2,color='b')
pomrzecz=[]
for i in range(0,len(results)):
    pomrzecz.append(abs(results[i]-avgres))
pomrzecz.sort()
deltarzecz=pomrzecz[math.ceil((1-alfa)*len(pomrzecz))]
yrzecz1=2*[avgres+deltarzecz]
yrzecz2=2*[avgres-deltarzecz]
plt.plot(xrange,yrzecz1,color='limegreen',label='Rzeczywistość, α='+str(1-alfa))
plt.plot(xrange,yrzecz2,color='limegreen')
deltachern=2.82210997581402 # ex=1, alfa=0.1
ychern1=2*[avgres+deltachern]
ychern2=2*[avgres-deltachern]
plt.plot(xrange,ychern1,color='hotpink',label='Chernoff, α='+str(1-alfa))
plt.plot(xrange,ychern2,color='hotpink')
yavg=2*[avgres]
plt.plot(xrange,yavg,color='orangered',label='Średnia')

## Histogram ##
n=1000
nrep=1000
#plt.scatter(n,results[n-nMin],color='crimson',label='Badany punkt') # zaznaczenie badanego punktu
plt.legend()
plt.show()
hist_data=[]
for r in range(0,nrep):
    p=random_permutation(n)
    hist_data.append(fixed_points(p))
plt.hist(hist_data,color='k')
avg=statistics.mean(hist_data)
plt.axvline(x=avg,color='orangered',label='Średnia')
# Czebyszew
alfa=0.9
deltaczeb=math.sqrt(statistics.variance(hist_data)/(1-alfa))
plt.axvline(x=avg+deltaczeb,color='b',label='Czebyszew, α='+str(alfa))
plt.axvline(x=avg-deltaczeb,color='b')
# Chernoff # !!! błąd jest ewidentny, bo lepiej niż rzeczywistość !!!
#deltachern=3.31621889700067 # punkty stałe # uwaga zmienić też label na wykresie #0.9, 0.85, 0.75: 3.31621889700067, 3.03243077853728, 2.65284714023292
deltachern=2.82210997581402 # punkty stałe # uwaga zmienić też label na wykresie #0.9, 0.85, 0.75: 2.82210997581402, 2.50992648434853, 2.08134311480557
#deltachern=7.6311551501992360998 # cykle #0.9: 1.02051624557677
#deltachern=55.6957443661478617524 # rekordy #0.9: 55.6957443661478617524
plt.axvline(x=avg+deltachern,color='hotpink',label='Chernoff, α=0.9')
plt.axvline(x=avg-deltachern,color='hotpink')
# Rzeczywistość
pomrzecz=[]
for i in range(0,len(hist_data)):
    pomrzecz.append(abs(hist_data[i]-avg))
pomrzecz.sort()
deltarzecz=pomrzecz[math.ceil((alfa)*len(pomrzecz))]
plt.axvline(x=avg+deltarzecz,color='limegreen',label='Rzeczywistość, α='+str(alfa))
plt.axvline(x=avg-deltarzecz,color='limegreen')

plt.title('Liczba punktów stałych losowej permutacji,\nn='+str(n)+ ',\nliczba próbek='+str(nrep))
plt.xlabel('Liczba punktów stałych')
plt.ylabel('Liczba próbek')
plt.legend()
plt.show()
