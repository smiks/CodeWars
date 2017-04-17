unsigned int collatz(unsigned int n, unsigned int steps){
    if(n == 1)
      return steps;
    
    return n%2 == 0 ? collatz(n/2, steps+1) : collatz(3*n+1, steps+1);
}

unsigned int hotpo(unsigned int n){
    if(n == 0) return 0; //Optional Handler to n = 0
    return collatz(n, 0);
}