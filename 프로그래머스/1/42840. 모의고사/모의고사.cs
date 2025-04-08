using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] answers) 
    {
        int[] p1 = {1,2,3,4,5};
        int[] p2 = {2,1,2,3,2,4,2,5};
        int[] p3 = {3,3,1,1,2,2,4,4,5,5};
        
        int[] answer = new int[3];
        
        for(int i = 0; i <answers.Length; i++)
        {
            if(answers[i] == p1[i%p1.Length])
                answer[0]++;
            if(answers[i] == p2[i%p2.Length])
                answer[1]++;
            if(answers[i] == p3[i%p3.Length])
                answer[2]++;
        }
        
        int maxScore = answer.Max();
        
        List<int> result = new List<int>();
        
        for(int i = 0; i <answer.Length; i++)
        {
            if(answer[i] == maxScore)
                result.Add(i+1);
        }
        return result.ToArray();
    }
}