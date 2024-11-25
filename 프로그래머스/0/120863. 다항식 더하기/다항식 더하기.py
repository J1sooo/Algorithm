def solution(polynomial):
    polynomial=polynomial.replace('+','').split()
    xcount=0
    ncount=0
    
    for i in polynomial:
        if 'x' == i:
            xcount+=1
        elif i.isdigit():
            ncount+=int(i)
        else:
            xcount+=int(i.replace('x',''))
            
    if xcount==0:
        return str(ncount) if ncount!=0 else "0"
    elif xcount==1:
        return 'x + ' + str(ncount) if ncount!=0 else 'x'
    elif xcount>0:
        return f'{xcount}x + ' + str(ncount) if ncount!=0 else f'{xcount}x'
    