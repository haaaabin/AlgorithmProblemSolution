using System;
using System.Collections.Generic;
using System.Linq;

class Solution {
    public int solution(int[,] maps) {
        int n = maps.GetLength(0);
        int m = maps.GetLength(1);
        
        int[,] visited = new int[n,m];
        Queue<(int x, int y)> q = new Queue<(int, int)>();
        
        int[] dx = {-1,1,0,0};
        int[] dy = {0,0,-1,1};
        
        q.Enqueue((0,0));
        visited[0,0] = 1;
        
        while (q.Count > 0)
        {
            var (x,y) = q.Dequeue();
            
            for(int i = 0; i < 4; i++)
            {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx,ny] == 1 && visited[nx,ny] == 0)
                {
                    q.Enqueue((nx,ny));
                    visited[nx,ny] = visited[x,y] + 1;
                }
            }
        }
        if(visited[n-1,m-1] == 0)
            return -1;
        else
            return visited[n-1,m-1];
    }
}