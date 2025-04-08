using System;
using System.Collections.Generic;
using System.Linq; 

public class Solution {
    public int solution(int[] priorities, int location) {
        Queue<(int idx, int priority)> q = new Queue<(int,int)>();
        for(int i = 0; i < priorities.Length; i++)
        {
            q.Enqueue((i, priorities[i]));
        }
        
        int answer = 0;
        
        while (q.Count > 0)
        {
            var process = q.Dequeue();
            
            if (q.Any(x=> x.priority > process.priority))
            {
                q.Enqueue(process);
            }
            else
            {
                answer++;
                
                if(process.idx == location)
                {
                    return answer;
                }
            }
        }
        
        return answer;
    }
}