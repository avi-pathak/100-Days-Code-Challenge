//https://www.hackerrank.com/challenges/variadic-functions-in-c/problem
int sum(int count, ...)
{
    va_list ap;
    int t = 0;
    va_start(ap, count);
    while (count--)
    {
        t += va_arg(ap, int);
    }
    return t;
}

int min(int count, ...)
{
    va_list ap;
    int t = MAX_ELEMENT;
    va_start(ap, count);
    while (count--)
    {
        int i = va_arg(ap, int);
        t = Min(t, i);
    }
    return t;
}
