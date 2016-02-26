def special_min(P):
    if P == 1:
        return 1
    else:
        return special_min((P+1)/2)+1
    


for case_no in xrange(1,int(raw_input())+1):
    D = raw_input()
    P = max(map(int,raw_input().split()))
    ans = special_min(P)

    print 'case #%d: %d' % (case_no,ans)