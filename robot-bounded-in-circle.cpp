class Solution {
public:
    bool isRobotBounded(string instructions) {
        int x = 0, y = 0, dx = -1, dy = 0, temp;
        for(auto ch: instructions){
            if(ch == 'L'){
                temp = -dy;
                dy = dx;
                dx = temp;
            }
            else if(ch == 'R'){
                temp = -dx;
                dx = dy;
                dy = temp;
            }
            else{
                x += dx;
                y += dy;
            }
        }
        if(dx != -1 || (x == 0 && y == 0)) return true;
        return false;
    }
};