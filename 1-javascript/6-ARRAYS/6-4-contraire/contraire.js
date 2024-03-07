// 4--contraire du tableau MASFOFA
let numbers1 = [1,2,3,4,5];
function reverse(arr){
    let temp = [];
    for(let i in arr)
        temp.unshift(arr[i]);
    return temp;    
}
console.log(reverse(numbers1));
console.log((numbers1));
