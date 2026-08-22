class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Build dictionaries for each, 
        
        then adding a value for each time a character apppears. 
        
        Then if both dictionaries are the same return true. 
        '''

        s_dict = {}
        t_dict = {}

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        if s_dict == t_dict:
            return True
        else:
            return False