class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        cow = sum([s == t for s,t in zip(secret,  guess)])
        bull = 0
        secret_map =  {}
        for s in secret:
            if s not in secret_map:
                secret_map[s] = 1
            else: 
                secret_map[s] += 1
        
        for g in guess:
            if g not in secret_map or secret_map[g] == 0:
                print g, secret_map
                continue
            else:
                secret_map[g] -= 1
                bull += 1
        return ''.join([str(cow), 'A', str(bull-cow), 'B'])

# simpler expression
s, g = Counter(secret), Counter(guess)
a = sum(i == j for i, j in zip(secret, guess))
return '%sA%sB' % (a, sum((s & g).values()) - a)

b = Solution()
print b.getHint("4321","1243")



# faster solution
secret_map, guess_map = {}, {}
bull_count, cow_count = 0, 0
for i in range(len(secret)):
    if secret[i] == guess[i]:
        bull_count += 1
    else:
        if secret[i] in secret_map:
            secret_map[secret[i]] += 1
        else:
            secret_map[secret[i]] = 1
        if guess[i] in guess_map:
            guess_map[guess[i]] += 1
        else:
            guess_map[guess[i]] = 1
for i in guess_map:
    if i in secret_map:
        cow_count += min(secret_map[i], guess_map[i])
return '%sA%sB' % (bull_count, cow_count)