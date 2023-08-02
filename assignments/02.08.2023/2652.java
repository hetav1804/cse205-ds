lass Solution {
    int i,sum;
    public int sumOfMultiples(int n) {
       for(i=1;i<=n;i++)
       {
           if(i%3==0 || i%5==0 || i%7==0)
           sum=sum+i;
       } 
       return sum;
    }
}