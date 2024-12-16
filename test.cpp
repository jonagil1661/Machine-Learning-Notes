#include <iostream>
#include <vector>
int main() {
  std::cout << "hello" << std::endl;
std::string s = "abacaba";
    std::vector<std::string> list;
        list.push_back(std::string(1, s[0]));
        for (int i = 1; i < s.size(); i++) {
            if (s.at(i) == s.at(i-1)) {
                list.push_back(std::string(1, s[i]));
            } else {
                int l = list.size() - 1;
                list[l] += std::string(1, s[i]);
            }
        }
        for ( int i = 0; i < list.size() ; i++) {
            std::cout << list[i] << " " << std::endl;
        }

  return 0;
}