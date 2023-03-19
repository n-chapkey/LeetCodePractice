/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    const map_s_t = {};
    const map_t_s = {};
    for(let i in s){
        if(map_s_t[s[i]] && map_s_t[s[i]] !== t[i]){
            return false;
        }else if(map_t_s[t[i]] && map_t_s[t[i]] !== s[i]){
            return false
        }else{
            map_s_t[s[i]] = t[i];
            map_t_s[t[i]] = s[i];
        }
    }
    
    return true;
};