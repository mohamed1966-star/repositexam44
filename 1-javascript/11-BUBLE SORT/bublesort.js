function bubleSort(array){
    let swapped;
    do{
        swapped = false;
        for(let i = 0 ; i < array.length ; i++){
            if(array[i] > array[i+1]){
                let tmp = array[i];
                array[i] = array[i+1];
                array[i+1] = tmp;
                swapped = true;
            }
        }
    } while(swapped)
    return array;
}
let sorted = bubleSort([5,1,4,2,8]);
console.log(sorted);
console.log('---------------------------------------');
//
// EASY
const numbers = [5,1,4,2,8];
numbers.sort((a,b) =>{
    return a-b;    
});
console.log(numbers);



