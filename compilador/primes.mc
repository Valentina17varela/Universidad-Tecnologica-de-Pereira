// Imprime los numeros primos entre 2-100,
// usando el algoritmo de Eratostenes
fun isprime(n) {
    var factor = 2;
    while (factor * factor <= n) {
        if (n % factor == 0) {
            return false;
        }
        factor = factor + 1;
    }
    return true;
}

for (var n = 2; n <= 100; n = n + 1) {
    if (isprime(n)) {
        print n;
    }
}