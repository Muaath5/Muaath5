//// Cards trick
#include <vector>
#include <math.h>
#include <algorithm>


#include <iostream>
#define INPUT_ERROR cout << "Input Error\n";
using namespace std;

#define all(x) x.begin(),x.end()
#define ll long long

struct card {
	int type; // 1 = Hearts, 2 = Diamond, 3 = Shiriah, 4 = Speat
	int shape; // From 0 to 12
	friend bool operator < (const card& x, const card& y) {
		return pow(x.shape, x.type) < pow(y.shape, y.type);
	}
	friend bool operator <= (const card& x, const card& y) {
		return pow(x.shape, x.type) <= pow(y.shape, y.type);
	}
	friend bool operator == (const card& x, const card& y) {
		return pow(x.shape, x.type) == pow(y.shape, y.type);
	}
	friend bool operator > (const card& x, const card& y) {
		return pow(x.shape, x.type) > pow(y.shape, y.type);
	}
	friend bool operator >= (const card& x, const card& y) {
		return pow(x.shape, x.type) >= pow(y.shape, y.type);
	}
	friend bool operator != (const card& x, const card& y) {
		return pow(x.shape, x.type) != pow(y.shape, y.type);
	}
};

vector<card> exclude(vector<card> cards) // five cards always
{
	// 1. Find duplicate
	card c1, c2;
	int c1idx = -1, c2idx = -1;
	for (int i = 0; i < cards.size(); i++) {
		for (int j = i+1; j < cards.size(); j++) {
			if (cards[i].type == cards[i].type) {
				c1 = cards[i], c2 = cards[j];
				c1idx = i, c2idx = j;
				i = 100;
				break;
			}
		}
	}
	if (c1idx == -1 || c2idx == -1) {
		INPUT_ERROR;
		return {};
	}
	int diff = abs(c1.shape - c2.shape);
	if (diff > 6)
		if (c2.shape > c1.shape) swap(c1, c2);
		else
			if (c2.shape < c1.shape) swap(c1, c2);
	// C2 = (C1 + N) % 13
	// Find N
	int n = 0;
	for (int i = 1; i <= 6; i++)
	{
		if (c2.shape == (c1.shape + i) % 13) {
			n = i;
			break;
		}
	}
	n--;
	cards.erase(cards.begin() + c1idx);
	cards.erase(cards.begin() + c2idx - (c1idx < c2idx));

	while (n--)
		next_permutation(cards.begin(), cards.end());
	cards.insert(cards.begin(), { c1 });
	return cards;
}

card missing(vector<card> cards) // four cards always
{
	card c1 = cards[0];
	cards.erase(cards.begin());

	auto cpy = cards;
	sort(all(cpy));
	int n = 1;
	while (cpy != cards) {
		next_permutation(all(cpy));
		n++;
	}
	return card{ c1.type, (c1.shape + n) % 13 };
}


char num_to_char(int num)
{
	if (num == 0) return 'A';
	if (num == 10) return 'J';
	if (num == 11) return 'Q';
	if (num == 12) return 'K';
}

// Manuall Grader

int main()
{
	char cmd;
	while (cin >> cmd && cmd != 'q')
	{
		vector<card> v;
		if (cmd == 'm')
		{
			v.resize(4);
			for (int i = 0; i < 4; i++)
				cin >> v[i].type >> v[i].shape;
			card mis = missing(v);
			cout << "===\n";
			cout << mis.type << ' ' << mis.shape << '\n';
		}
		if (cmd == 'e')
		{
			v.resize(5);
			for (int i = 0; i < 5; i++)
				cin >> v[i].type >> v[i].shape;
			vector<card> res = exclude(v);
			cout << "===\n";
			for (card c : res)
				cout << c.type << ' ' << c.shape << '\n';
		}
	}
}