"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        buff_dict = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'] ,
                     '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'],
                     '8':['t','u','v'], '9':['w','x','y','z']}
        for i in range(len(digits)):
            if digits[i] == '0' or digits[i] == '1':
                return []
            elif res == []:
                res = buff_dict[digits[i]]
            else:
                buff_list = []
                for item1 in res:
                    for item2 in buff_dict[digits[i]]:
                        buff_list.append(item1+item2)
                res = buff_list

        return res