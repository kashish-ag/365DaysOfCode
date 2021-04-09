#Question Link: https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        s=""
        for i in range(len(command)):
            if(command[i]=="G"):
                s=s+"G"
            
            elif(command[i]=="(" and command[i+1]=="a"):
                s=s+"al"
            
            elif(command[i]=="(" and command[i+1]==")"):
                s=s+"o"
            else:
                continue
            
        return s
