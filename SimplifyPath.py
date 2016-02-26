class Solution(object):

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s = path.split('/')
        stack = []
        for c in s:

            if c not in ['.', '..', '']:
                stack.append('/')
                stack.append(c)

            if c == '..' and stack != []:
                stack.pop()
                stack.pop()

        if not stack:
            return '/'
        else:
            return ''.join(stack)
