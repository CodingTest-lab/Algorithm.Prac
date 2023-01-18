class Solution {
    public int solution(int n, int k) {
            int i = n/10;
            int answer = n*12000 + k*2000 - i*2000;
            return answer;
        }   
    }