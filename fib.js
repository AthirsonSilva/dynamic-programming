const fib = (n) => {
    // Base case
    if (n <= 2) return 1

    // Recursive case
    return fib(n - 1) + fib(n - 2) // O(2^n) time complexity (exponential)

    // O(n) space complexity
}

console.log(fib(6))
console.log(fib(60))

