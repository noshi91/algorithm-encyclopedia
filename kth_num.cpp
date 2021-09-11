#include <cstddef>
#include <functional>
#include <set>

template <class T, class Compare = std::less<T>> class kth_num {
  std::multiset<T, Compare> low;
  std::multiset<T, Compare> high;

public:
  kth_num(const Compare &comp = Compare()) : low(comp), high(comp) {}

  void insert(const T &x) {
    low.insert(x);
    const auto itr = std::prev(low.end());
    high.insert(*itr);
    low.erase(itr);
  }

  void erase(const T &x) {
    const auto itr = low.find(x);
    if (itr != low.end()) {
      low.erase(itr);
      return;
    }
    const auto itr2 = high.find(x);
    if (itr2 != high.end()) {
      high.erase(itr2);
    }
  }

  std::size_t size() const { return low.size() + high.size(); }

  T kth(const std::size_t k) {
    assert(k < size());
    while (low.size() < k) {
      const auto itr = high.begin();
      low.insert(*itr);
      high.erase(itr);
    }
    while (low.size() > k) {
      const auto itr = low.begin();
      high.insert(*itr);
      low.erase(itr);
    }
    return *high.begin();
  }
};
