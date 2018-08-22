
ref 

https://www.cnblogs.com/jiangchen/p/5393849.html

回溯算法也算是遍历算法的一种，回溯算法是对Brute-Force算法的一种改进算法，一个典型的应用是走迷宫问

1、概念
回溯算法实际上一个类似枚举的搜索尝试过程，主要是在搜索尝试过程中寻找问题的解，当发现已不满足求解条件时，就“回溯”返回，尝试别的路径。

回溯法是一种选优搜索法，按选优条件向前搜索，以达到目标。但当探索到某一步时，发现原先选择并不优或达不到目标，就退回一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”。

回溯法（英语：backtracking）也称试探法，回溯法有“通用的解题方法”之称。它可以系统的搜索一个问题的所有解或者任意解。

回溯法是一个既带有系统性又带有跳跃性的的搜索算法。它在包含问题的所有解的解空间树中，按照深度优先的策略，从根结点

出发搜索解空间树。算法搜索至解空间树的任一结点时，总是先判断该结点是否肯定不包含问题的解。如果肯定不包含，则跳过

对以该结点为根的子树的系统搜索，逐层向其祖先结点回溯。否则，进入该子树，继续按深度优先的策略进行搜索。回溯法在用来

求问题的所有解时，要回溯到根，且根结点的所有子树都已被搜索遍才结束。而回溯法在用来求问题的任一解时，只要搜索到问题

的一个解就可以结束。这种以深度优先的方式系统地搜索问题的解的算法称为回溯法，它适用于解一些组合数较大的问题.

回溯法通常用最简单的递归方法来实现，在反复重复上述的步骤后可能出现两种情况：

1 .找到一个可能存在的正确的答案。

2. 在尝试了所有可能的分步方法后宣告该问题没有答案。

在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。

2、适用范围
在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根结点出发深度探索解空间树。

 适用范围：

1，问题的解用向量表示

  X = (x1, x2, ..., xn)

2，需要搜索一个或一组解

3，满足约束条件的最优解

等

回溯法的基本思想
对于用回溯法求解的问题，首先要将问题进行适当的转化，得出状态空间树。这棵树的每条完整路径都代表了一种解的可能。通过深度优先搜索

这棵树，枚举每种可能的解的情况；从而得出结果。但是，回溯法中通过构造约束函数，可以大大提升程序效率，因为在深度优先搜索的过程中，

不断的将每个解（并不一定是完整的，事实上这也就是构造约束函数的意义所在）与约束函数进行对照从而删除一些不可能的解，这样就不必继续

把解的剩余部分列出从而节省部分时间。

回溯法中，首先需要明确下面三个概念：

 1，约束函数：约束函数是根据题意定出的。通过描述合法解的一般特征用于去除不合法的解，从而避免继续搜索出这个不合法解的剩余部分。因此，

       约束函数是对于任何状态空间树上的节点都有效、等价的。

2，状态空间树：刚刚已经提到，状态空间树是一个对所有解的图形描述。树上的每个子节点的解都只有一个部分与父节点不同。

3，扩展节点、活结点、死结点：所谓扩展节点，就是当前正在求出它的子节点的节点，在DFS中，只允许有一个扩展节点。活结点就是通过与约束函数

      的对照，节点本身和其父节点均满足约束函数要求的节点；死结点反之。由此很容易知道死结点是不必求出其子节点的（没有意义）。

3、用回溯法解题的一般步骤：
首先，要通过读题完成下面三个步骤：


(1)描述解的形式，定义一个解空间，它包含问题的所有解，这一步主要明确问题的解空间树。

(2)构造状态空间树。

(3)构造约束函数（用于杀死节点）。

然后就要通过DFS思想完成回溯，具体流程如下：

(1)设置初始化的方案（给变量赋初值，读入已知数据等）。

(2)变换方式去试探，若全部试完则转(7)。

(3)判断此法是否成功（通过约束函数），不成功则转(2)。

(4)试探成功则前进一步再试探。

(5)正确方案还未找到则转(2)。

(6)已找到一种方案则记录并打印。

(7)退回一步（回溯），若未退到头则转(2)。

(8)已退到头则结束或打印无解。

 

总结起来就是: 

针对所给问题，确定问题的解空间 --> 确定结点的扩展搜索规则--> 以DFS方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。

4、算法框架
（1）问题框架

设问题的解是一个n维向量(a1,a2,………,an),约束条件是ai(i=1,2,3,…..,n)之间满足某种条件，记为f(ai)。

（2）非递归回溯框架

复制代码
int a[n],
i;初始化数组a[];
i = 1;
while (i > 0(有路可走) and(未达到目标)) // 还未回溯到头
{
    if (i > n) // 搜索到叶结点
    {搜索到一个解，输出；
    } else // 处理第i个元素
    {
        a[i]第一个可能的值；
        while (a[i]在不满足约束条件且在搜索空间内) {
            a[i]下一个可能的值；
        }
        if (a[i]在搜索空间内) {
            19 : 标识占用的资源；20 : i = i + 1; // 扩展下一个结点  21:          }  22:          else  23:         {
            清理所占的状态空间； // 回溯25:               i = i –1; 
        }
    }
复制代码
 

（3）递归的算法框架

回溯法是对解空间的深度优先搜索，在一般情况下使用递归函数来实现回溯法比较简单，其中i为搜索的深度，框架如下：

复制代码
int a[n];
    try(int i)
    {
        if(i>n)
           输出结果;
         else
        {
           for(j = 下界; j <= 上界; j=j+1)  // 枚举i所有可能的路径
           {
              if(fun(j))                 // 满足限界函数和约束条件
                {
                   a[i] = j;
                ...                         // 其他操作
                   try(i+1);
                 回溯前的清理工作（如a[i]置空值等）;
                 }
            }
        }
   }
复制代码
典型问题应用
素数环问题，hdoj1016：http://acm.hdu.edu.cn/showproblem.php?pid=1016

题目大意：

将从1到n这n个整数围成一个圆环，若其中任意2个相邻的数字相加，结果均为素数，那么这个环就成为素数环。

要求输出：从整数1开始。

分析问题，可以构造解空间树，比较顺利的想到 DFS 、回溯。

代码如下：

复制代码
 1 #include<stdio.h>  
 2 #include <string.h>  
 3   
 4 #define M 40  
 5   
 6 int isPrime[M];////素数表,下标为素数的置为1,否则0  
 7 int vis[M>>1];// vis 标识 1-n,是否被选  
 8 int res[M>>1];// 存储解向量  
 9   
10 int cnt;// 测试样例个数  
11   
12 void prime()//求出1-40的所有素数  
13 {  
14     int i, j;  
15     for(i=1; i<M; ++i)  
16     {  
17         int ok = 1;  
18         for(j=2; j*j<=i; ++j)  
19         {  
20             if(i%j == 0)  
21             {  
22                 ok = 0;  
23                 break;  
24             }  
25         }  
26         if(ok)  
27             isPrime[i]=1;  
28   
29     }  
30 }  
31   
32 void dfs(int cur, int n)  
33 {  
34     int i;  
35     if(cur == n && isPrime[res[n-1] + res[0]])//别忘了测试边界，最后一个和第一个数 构成的环  
36     {  
37         for(i=0; i<n-1; ++i)  
38             printf("%d ", res[i]);  
39         printf("%d\n", res[i]);  
40     }  
41     else  
42     {  
43         for(i=2; i<=n; i++)// 尝试每个i, 1始终在排头,因此从2开始计算  
44         {  
45             if(!vis[i] && isPrime[res[cur-1] + i])// i未用过且和前一个数和为素数  
46             {  
47                 res[cur] = i;  
48                 vis[i] = 1; // 设置标志  
49                 dfs(cur+1, n);  
50                 vis[i] = 0; // 回溯, 清除标识  
51             }  
52         }  
53     }  
54 }  
55   
56   
57 int main()  
58 {  
59     int n;  
60     //freopen("in.txt", "r", stdin);  
61     prime();  
62     cnt = 0;  
63     while(scanf("%d", &n) != EOF)  
64     {  
65         ++cnt;  
66         printf("Case %d:\n", cnt);  
67         memset(vis, 0, sizeof(vis));  
68         res[0] = 1;  
69         dfs(1, n);  
70         printf("\n");  
71     }  
72     return 0;  
73 }  
复制代码
代码中 prime()函数 求出1-40的所有素数，因为只要测试 1-19 因此 可以事前 把1-38的素数存储到一个 素数表里。这样计算时间更快。