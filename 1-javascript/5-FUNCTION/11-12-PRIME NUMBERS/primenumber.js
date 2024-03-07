let num = prompt('Enter number to check :');
function isPrime(num){
    for(let i=2; i< num; i++){
        if(num % i === 0) return false;
    }
    return num > 1;
}

function primes(max){
    for(let i=2; i< max; i++)
        if(isPrime(i)) console.log(i);
}
//let num = prompt('Enter number to check :');
primes(num);
/*console.log('--------------------------------------------');
//RECURSION
function factorial(n){
    return n===0?1:n * factorial(n-1);
}
console.log(factorial(3));*/
