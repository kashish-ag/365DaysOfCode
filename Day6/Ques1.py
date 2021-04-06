#Question Link: https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=""
        l=address.split(".")
        for i in l:
            a=a+i+"[.]"
        return a[:-3]
