# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         charDictList = []
#         for word in strs:
#             dictionary = {}

#             for char in word:
#                 if char in dictionary:
#                     dictionary[char] += 1
#                 else:
#                     dictionary[char] = 1
                
#             charDictList.append(dictionary)
        
#         groupList = []
#         groupDict = {}
#         for i in range(len(charDictList)):
#             if charDictList[i] not in groupDict:
#                 groupDict[charDictList[i]] = count
#                 groupList[count].append(strs[i])
#                 count += 1
#             else:
#                 index = groupDict[list]
#                 goupList[index].append[strs[i]]
                
#         return groupList
                
            
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            a = list(s)
            a.sort()
            a = ''.join(a)
            if a not in dic:
                dic[a] = [s]
            else:
                dic[a].append(s)
        result = []
        for s in dic:
            dic[s].sort()
            result.append(dic[s])
        return result
                

# map + lambda + list comprehension = 3 Lines of Python

def anagrams(self, strs):
    dic = defaultdict(list)
    map(lambda item: dic[''.join(sorted(item))].append(item), strs)
    return [x for key in dic.keys() for x in dic[key] if len(dic[key]) > 1]

# 2 lines python
count = collections.Counter([tuple(sorted(str)) for str in strs])
return filter(lambda x: count[tuple(sorted(x))] > 1, strs)


def anagrams(self, strs):
    dic = defaultdict(list)
    for item in strs:
        after = ''.join(sorted(item))
        dic[after].append(item)
    ans = []
    for item in dic:
        values = dic[item]
        if len(values) > 1:
            ans.extend(values)
    return ans
