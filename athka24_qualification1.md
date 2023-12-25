<div dir="auto">
  
 # حلول الاختبار التأهيلي أذكى 2024 بلغة C++


كتب هذا الملف:
- معاذ القرني
- يزن آشي
وهذا الملف ملكية [قناة أذكى](https://t.me/MawhibaNOPAI)


| الاسم            | الدرجة   | هل تختلف المعطيات بين الطلاب؟  |
|-----------------|-------|------------------------|
|  الجملة الشرطية  IF  | 20    | نعم                     |
| التكرار           | 31     | نعم                    |
|  معادلة خالد       | 37     | نعم                    |
|  الاستدعاء الذاتي لعبير | 40    | نعم                    |
|  واجب ريم المنزلي   | 42    | نعم                    |
|  الأعداد الجيدة      | 43    | نعم                    |
|  المجموعة الجزئية    | 44    | لا                    |

##  الجملة الشرطية IF 
**الفكرة:** ننسخ الكود ونضيف أمر طباعة للمتغير المطلوب
<details style="padding: 10px">
  <summary>الحل بلغة С++</summary>

```c++
#include <iostream>
using namespace std;
int main()
{
  int x = 11;
  int y = 29;
  int z;

  if (x % 2 != 0) {
    if (x > y) {
        z = 0;
    } else {
        z = 1;
    }
  } else {
    if (x > y) {
        z = 2;
    } else {
        z = 3;
    }
  }
  cout << z; // أضفنا أمر الطباعة
}
```

</details> 

## التكرار
**الفكرة:** ننسخ الكود ونضيف أمر طباعة للمتغير المطلوب

<details style="padding: 10px">
  <summary>الحل بلغة C++</summary>

```c++
#include <iostream>
using namespace std;
int main()
{
  int r = 0;    
  for (int i = 0; i < 100; i++) {
  	r = (277 * r + 241) % 433;
  }
  cout << r; // أضفنا أمر الطباعة
}
```
  
</details>

##  معادلة خالد 
**الفكرة:** تجربة جميع الاحتمالات


<details style="padding: 10px">
  <summary>الحل بلغة C++</summary>

```c++
#include <iostream>
using namespace std;

const int P = 35171; // معطيات المسألة
const int A = 24636; // معطيات المسألة

int main()
{
    for (long long x = 1; x <= 1000000; x++)
    {
        if (x * A % P == 1)
        {
            cout << x;
            break;
        }
    }
}
```
  
</details>

##  الاستدعاء الذاتي لعبير 

<details style="padding: 10px">
  <summary>خوارزمية الاستدعاء الذاتي (ريكيرجن / Recursion)</summary>

**الفكرة:** تطبيق العطيات بتحويل المسألة إلى دالة ثم استدعائها كل مرة، وتذكر النتائج السابقة (memoization)

  
<details style="padding: 10px">
  <summary>الحل بلغة C++</summary>

```c++
#include <iostream>
using namespace std;

const int N = 257; // اكتب الرقم المطلوب
const int MOD = 193; // اكتب الرقم بعد باقي القسمة

int memo[N+1];
int rec(int i)
{
    if (memo[i] != -1)
        return memo[i];
    return memo[i] = (rec(i-3) + rec(i-2) * rec(i-1)) % MOD;
}

int main()
{
    memset(memo, -1, sizeof memo);
    memo[1] = 1;
    memo[2] = 2;
    memo[3] = 3;
    cout << rec(N);
}
```
  
</details>

</details>


<details>
  <summary>الحل باستخدام البرمجة الديناميكية (Dynamic Programming / DP)</summary>
  <b>الفكرة: تطبيق المعادلة كما هي</b>

```c++
#include <iostream>
using namespace std;

const int N = 257; // اكتب الرقم المطلوب
const int MOD = 193; // اكتب الرقم بعد باقي القسمة

int dp[N+1];

int main()
{
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 3;
    for (int i = 4; i <= N; i++)
        dp[i] = (dp[i-3] + dp[i-2] * dp[i-1]) % MOD;
    cout << dp[N];
}
```
  
</details

##  واجب ريم المنزلي


<details style="padding: 10px">
  <summary>البحث الثنائي (Binary Search)</summary>

**الفكرة:** وجود حد أعلى للإجابة (نسميه $أ$) وحد أعلى للإجابة (نسميه $ب$)، ثم نختار عدد في المنتصف $\frac{ب + أ}{2}$، ونغير الحد الأدنى والأعلى بناءً على نتيجة الدالة لهذا الرقم.

**ملاحظة:** يمكن تطبيق هذه الفكرة يدويًا باستعمال الحاسبة أو برامج الرسم البياني دون الحاجة لكتابة برنامج
<details style="padding: 10px">
  <summary>الحل بلغة C++</summary>

```c++
#include <bits/stdc++.h>
using namespace std;

const long double Y = 482.15385787945286;
const long double PREC = 1e-4;

#define f(x) (x+exp(x/100))

int main()
{
    long double l = 1, r = 10000;
    while (abs(l - r) > PREC)
    {
        long double mid = (l + r) / 2;
        if (f(mid) <= Y)
            l = mid;
        else
            r = mid - PREC;
    }
    cout << fixed << setprecision(4) << l;
}
```

</details>
</details>

##  الأعداد الجيدة 

<details>
  <summary>الحل بلغة C++</summary>

```c++
#include <bits/stdc++.h>
using namespace std;

const int L = 207418; // نضع هنا قيم المعطيات 
const int R = 691140; // نضع هنا قيم المعطيات 

bool isgood(int xx)
{
    string x = to_string(xx);
    int a=x[0]-'0';
    int b=x[1]-'0';
    int c=x[2]-'0';
    int d=x[3]-'0';
    int e=x[4]-'0';
    int f=x[5]-'0';
    return (a*c+d*f) == (a+b)*e-f;
}

int main()
{
    int sol = 0;
    for (int i = L; i <= R; i++)
        sol += isgood(i);
    cout << sol;
}
```
  
</details>




##  المجموعة الجزئية 


<details>
  <summary>تجربة كل الاحتمالات مع خوارزمية الالتقاء في المنتصف (Meet in the middle) باستعمال الاستدعاء الذاتي (Recursion)</summary>

**الفكرة:** بما أن عدد الاحتمالات عالي جدًا ($= 2^{40} = 10^{12}$ 1 ترليون)، واللغات في المتوسط تنجز ($= 10^8$ 100 مليون) عملية في الثانية، يعني أن البرنامج لو جرب كل الاحتمالات سيستغرق حوالي ساعتين ونصف!

**الاختصار:** نقسم مجموعة الأعداد إلى نصفين، ونجرب جميع الاحتمالات في كل نصف، ثم نجرب كل احتمالات الدمج ونستعمل البحث الثنائي للاختصار الإضافي
                
```c++
#include <bits/stdc++.h>
#define ll long long

using namespace std;

const int a[] = {1697976, 1970865, 1481237, 1583430, 
1537387, 1270113, 1184765, 1668778, 1857442, 1658671, 
1349846, 1399258, 1636211, 1887763, 1659794, 1277974, 
1438563, 1645195, 1161182, 1991079, 1295942, 1848458, 
1932683, 1759741, 1394766, 1267867, 1664286, 1176904, 
1125246, 1210594, 1950651, 1638457, 1927068, 1619366, 
1299311, 1490221, 1090433, 1678885, 1753003, 1347600};
const int C = 46342470;

vector<ll> sum, sum2;
const int n=40;

void rec(int idx, ll sum, int lim, vector<ll> &su)
{
    if (idx == lim) {
        su.push_back(sum);
        return;
    }
    rec(idx+1, sum+a[idx], lim, su);
    rec(idx+1, sum, lim, su);
}

int main()
{
    rec(0, 0, n/2, sum);
    rec(n/2, 0, n, sum2);
    
    sort(sum2.begin(), sum2.end());
    
    ll sol = 0;
    for (ll v1 : sum) {
        ll xx = *(upper_bound(sum2.begin(), sum2.end(), C-v1)-1);
        sol = max(sol, v1+xx);
    }
    cout << sol;
}
```
	
</details>


<details>
  <summary>تجربة كل الاحتمالات مع خوارزمية الالتقاء في المنتصف (Meet in the middle) باستعمال تمثيل الأرقام الثنائية (Bitmasks)</summary>

```c++
#include <bits/stdc++.h>
#define ll long long

using namespace std;

const int a[] = {1697976, 1970865, 1481237, 1583430, 
1537387, 1270113, 1184765, 1668778, 1857442, 1658671, 
1349846, 1399258, 1636211, 1887763, 1659794, 1277974, 
1438563, 1645195, 1161182, 1991079, 1295942, 1848458, 
1932683, 1759741, 1394766, 1267867, 1664286, 1176904, 
1125246, 1210594, 1950651, 1638457, 1927068, 1619366, 
1299311, 1490221, 1090433, 1678885, 1753003, 1347600};
const int C = 46342470;

vector<ll> sum, sum2;
const int n=40;

int main()
{   
    const int half = n / 2;
    for (int i = 0; i < (1 << half); i++)
    {
        ll s = 0;
        for (int j = 0; j < half; j++)
        {
            if (i & (1 << j))
                s += a[j];
        }
        sum.push_back(s);
    }
    
    for (int i = 1; i < (1 << half); i++)
    {
        ll s = 0;
        for (int j = half; j < n; j++)
        {
            if (i & (1 << (j - half)))
                s += a[j];
        }
        sum2.push_back(s);
    }
    
    sort(sum2.begin(), sum2.end());
    
    ll sol = 0;
    for (ll v1 : sum) {
        ll xx = *(upper_bound(sum2.begin(), sum2.end(), x-v1)-1);
        sol = max(sol, v1+xx);
    }
    cout << sol;
}
```

</details>
 
<details>
  <summary>الحل باستعمال البرمجة الديناميكية (Dynamic Programming / DP)</summary>

```c++
#include <bits/stdc++.h>
using namespace std;

int a[] = {1697976, 1970865, 1481237, 1583430, 
1537387, 1270113, 1184765, 1668778, 1857442, 1658671, 
1349846, 1399258, 1636211, 1887763, 1659794, 1277974, 
1438563, 1645195, 1161182, 1991079, 1295942, 1848458, 
1932683, 1759741, 1394766, 1267867, 1664286, 1176904, 
1125246, 1210594, 1950651, 1638457, 1927068, 1619366, 
1299311, 1490221, 1090433, 1678885, 1753003, 1347600};
const int C = 46342470;

const int N = 5e7; // أكبر قيمة ممكنة
int dp[N];

int main()
{
    dp[0] = 1;
    for (int i = 1; i <= 40; i++) {
        for (int j = N - 1; j > 0; j--) {
            if (j >= a[i]) {
                dp[j] |= dp[j - a[i]];
            }
        }
    }
    int result = 0;
    for (int i = 1; i <= C; i++)
    {
        if (dp[i])
            result = i;
    }
    cout << result;
}
```
        
  </details>

  
<details style="padding: 10px">
   <summary>تجربة احتمالات عشوائية</summary>

   <b>ملاحظة: هذه الفكرة قد تطبع أرقام خاطئة، لأنها تعتمد على العشوائية، لكن كل ما زادت عدد المحاولات زادت الدقة، وهي غالبًا تطبع نتائج صحيحة</b>
  
```c++
#include <bits/stdc++.h>
using namespace std;

int a[] = {1697976, 1970865, 1481237, 1583430, 
1537387, 1270113, 1184765, 1668778, 1857442, 1658671, 
1349846, 1399258, 1636211, 1887763, 1659794, 1277974, 
1438563, 1645195, 1161182, 1991079, 1295942, 1848458, 
1932683, 1759741, 1394766, 1267867, 1664286, 1176904, 
1125246, 1210594, 1950651, 1638457, 1927068, 1619366, 
1299311, 1490221, 1090433, 1678885, 1753003, 1347600};
const int C = 46342470;
const int TRIES = 1e5; // عدد المحاولات، 100 ألف محاولة

int main()
{
    int result = 0;
    for (int i=0; i <= TRIES; i++)
    {
        random_shuffle(a, a+n);
        int cur=0;
        for (auto c : v)
        {
            if (cur+c > C)
            {
                result = max(cur,result);
                break;
            }
            cur += c;
        }
    }
    cout << result;
}
```
        
</details>

</div>
