# Competitve Programming Complete Guides
## Online Judges
- [Codeforces](https://codeforces.com) organizes contests almost every week
- [CSES](https://cses.fi) contains a problemset of 300 problems
- [AtCoder](https://atcoder.jp) contains educational contests
- [SPOJ](https://spoj.com) has a random problemset
- [Leetcode](https://leetcode.com/problemset/) contains problems commonly used in interviews
- [CodeChef](https://codechef.com) there are some games you can play
- [OJ.UZ](https://oj.uz) contains problems from the olympics
- [HackerRank](https://www.hackerrank.com/domains/algorithms) educational problemset
- [VJudge](https://vjudge.net) is a website that you can see problems from +40 online judges

## Learning Resources
### Books
- [Competitive Programming Handbook (CPH)](https://cses.fi/book/book.pdf)
- [IUSACO Cpp](https://darrenyao.com/usacobook/cpp.pdf)

### Websites
- [USACO Guide](https://usaco.guide/)
- [CP Algorithms](https://cp-algorithms.com/)
- [GeeksForGeeks](https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/)

### Youtube Channels
- [Arabic Competitive Programming](https://www.youtube.com/@ArabicCompetitiveProgramming) 
- [Errichito](https://www.youtube.com/c/Errichto)

## Chinese Resources
- https://blog.xehoth.cc/
- https://oi.men.ci/
- https://memset0.cn/
- https://www.cnblogs.com/Ning-Mew/
- https://blog.csdn.net/cabi_zgx/article/details/79963427
- https://www.cnblogs.com/Paul-Guderian/

## IOI-Style Contests Hints
- At first read all the problems (that should be at most 30m), try to optimize this
- Spend about 40 minutes on easiest problem, then try to gather points
- Don't spend more than 1 consecutive hour on a single problem
- Take a little 1 or 2 breaks in the middle of the exam
- Debugging usually takes the whole time, don't let it steal your time. 

## Debugging Wrong Answer
- Check the constaints of the arrays
- Check if there is a code for input/output
- Check if there could be an overflow (usually caused by multiplication, powers, or factorial)
- Clear & Resize data-structures after each testcase
- Check the for loops starting & ending
- Check the binary search condition
- Handle the edge cases (i.e. 0, 1, even, odd, primes, etc..)
- Check sorting the array
- Make your code either all 0-based or all 1-based
- Check paranthesis when dealing with bitwise operations
- The size of segment tree should be <code>4*MAXN</code>
- Avoid comparing doubles using <code>==</code> or <code>!=</code>
- Avoid using <code>memset</code> with values other than 0 or -1
- Memorize the answers with indecies, if you sorted them at first
- Output <code>Case x: </code> Before calculating the answer
- In case of processing queries offline, do a <code>while</code> instead of <code>if</code> to check queries if it was somehow offline
- Don't forget <code>cout << fixed << setprecision(X);</code> if the output is double
- In intractive problems, remove fast i/o code
- Split your program to functions, especially in intractive problems
- In case of frequency array/map, check <code>++</code> instead of <code>=1</code>
- Don't forget endlines (<code>endl</code>, <code>'\n'</code>)
- Write a simulater program for the operations and output them
- Don't forget to handle the edge cases in two-pointers
- Don't rely on <code>#ifndef ONLINE_JUDGE</code>, Rely on some local defines
- Probably the given graph has loops, cycles, non-distinct edges
        
## Debugging Time/Memory Limit
<ol>
    <li>Calculate the <b>exact</b> time complexity of your code (Online Judges can handle ~$10^8$ complexity in 1 second)</code></li>
    <li>Calculate the <b>exact</b> memory complexity of your code and calculate memory limit in bytes</li>
    <li>Calculate the <b>exact</b> amount of interactions in your code (if the problem is interactive)</li>
    <li>Try to balance time & memory in the code</li>
    <li>Use <code>bitset</code> instead of boolean array to optimize memory</li>
    <li>Use fast i/o (<code>ios::sync_with_stdio(0),cin.tie(0),cout.tie(0)</code> in C++) and replace <code>endl</code> with <code>'\n'</code></li>
    <li>Add/Remove depending on system (32/64) <code>#define int long long</code></li>
    <li>Use <code>map</code> instead of <code>unordered_map</code>, (Or vice-versa)</li>
    <li>Use <code>set</code> instead of <code>unordered_set</code>, (Or vice-versa)</li>
    <li>Compress the numbers (i.e. Distinct Values Queries)</li>
    <li>Use array to count the frequencies instead of <code>map</code></li>
    <li><code>sqrt</code> takes long time, So use this <code>i*i <= n</code> is more effecient than <code>i <= sqrt(n)</code></li>
    <li>Optimize your seive from $O(N * \log_2{N})$ to $O(N * \log_2{\log_2{N}})$</li>
    <li>Don't clear the arrays & data-structures if there is no testcases</li>
    <li>Use array of sets instead of defining a <code>set</code> everytime</li>
    <li>Use memoization in recursion as much as possible</li>
    <li>Convert a recursive DP to an iterative DP</li>
    <li>Use <code>break</code>, <code>continue</code>, <code>goto</code>, and <code>return</code> as much as you could</li>
    <li>Use Porgan Princible (in 2SUM, you should add to the map while trying to find, not before)</li>
    <li>Use small-to-large decomposition (in trees or in DSU)</li>
    <li>Optimize memory in DP</li>
    <li>In finding shortest route path, put a matrix tells you were you came from, then roll back</li>
    <li>When rolling back to find a path, use a while instead of recursion</li>
    <li>In binary exponintiation, use <code>while</code> instead of recursion</li>
    <li>Write <code>const</code> in constant variables (i.e. <code>MOD</code>), because the compiler calculate it faster</li>
    <li>Write/Remove <code>inline</code> in functions that you are using</li>
    <li>In segment trees, building is faster than updating every element</li>
    <li>Pass parameters by reference if you can</li>
    <li>In DSU, use path compression + order by rank (small to large) optimizations, so your code runs in $O(\alpha(N))$</li>
    <li>Try different versions of the language (i.e. G++17, G++20, Clang20)</li>
    <li>If your code gets TLE on the edge, resubmitting the code may work</li>
    <li>If the solution of the problem is one of the subarrays, try to think how to convert it to two-pointers</li>
    <li>You may precalculate (hardcode) some values on local device and put them in your submission to optimize it</li>
    <li>You may use <code>#pragma</code> so read <a href="https://usaco.guide/adv/vectorization?lang=cpp">vectorization guide</a>, don't put it in your template, it may cause RTE in some online judges other than SOJ</li>
    <li>If non of these above worked, probably your algorithm is bad</li>
</ol>
