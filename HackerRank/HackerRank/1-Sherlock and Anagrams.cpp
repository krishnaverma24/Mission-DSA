int sherlockAndAnagrams(std::string s) {
    std::map<std::map<char,int>, int> unique_strings;
    int result = 0;
    for (size_t i = 0; i<s.size(); ++i){
        std::map<char,int> submap;
        for (size_t j = i; j<s.size(); ++j) {
            submap[s[j]]++;
            unique_strings[submap]++;
        }
    }
    for (auto& [substr, count]: unique_strings) {
        result += (count - 1)* count / 2;
    }
    return result;
}
