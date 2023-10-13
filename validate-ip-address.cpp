class Solution {
public:
    string validIPAddress(string queryIP) {
        bool is_ipv4 = (int)queryIP.find('.') == -1 ? 0 : 1;
        bool is_ipv6 = (int)queryIP.find(':') == -1 ? 0 : 1;
        if(!(is_ipv4^is_ipv6)) return "Neither";

        if(is_ipv4){
            int cnt = 0, n = 0, total = 0;
            for(auto ch: queryIP){
                if(isdigit(ch)){
                    if(cnt && !n) return "Neither";
                    cnt++;
                    n = n*10 + ch - '0';
                    if(n > 255) return "Neither";
                }
                else if(ch == '.'){
                    if(!cnt || n > 255) return "Neither";
                    cnt = n = 0;
                    total++;
                }
                else return "Neither";
            }
            if(!cnt || n > 255 || total != 3) return "Neither";
            return "IPv4";
        }
        if(is_ipv6){
            int cnt = 0, total = 0;
            for(auto ch: queryIP){
                if(isdigit(ch)) cnt++;
                else if(isalpha(ch)){
                    cnt++;
                    ch = tolower(ch);
                    if(ch > 'f') return "Neither";
                }
                else if(ch == ':'){
                    if(!cnt || cnt > 4) return "Neither";
                    total++;
                    cnt = 0;
                }
                else return "Neither";
            }
            if(!cnt || cnt > 4 || total != 7) return "Neither";
            return "IPv6";
        }
        return "";
    }
};