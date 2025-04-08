using System;

public class Solution {
    public int solution(int[,] sizes) {
        int w = 0;
        int h = 0;
        
        for (int i = 0; i <sizes.GetLength(0); i++)
        {
            int a = sizes[i,0];
            int b = sizes[i,1];
            if (a < b)
            {
                int temp = a;
                a = b;
                b = temp;
            }
            w = Math.Max(w,a);
            h = Math.Max(h,b);
        }
        return w * h;
    }
}