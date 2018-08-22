
ref 

https://www.cnblogs.com/jiangchen/p/5393849.html

backtracking 是非常general 的（也是一种遍历算法）

而dfs 是一种特殊的和tree结构有关的 backtracking 算法


回溯法用于搜索解(全部或者一个)，dp找最优解


https://www.cnblogs.com/python27/p/3989435.html

```C
bool Solve(configuration conf)
{
    if (no more choice)
        return (conf is goal state);

    for (all available choices)
    {
        try choice c;

        ok = solve(conf with choice c made);
        if (ok)
            return true;
        else
            unmake c;
    }

    retun false;
}
```
