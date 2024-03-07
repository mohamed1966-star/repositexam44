// Repparer les fautes
// 3-  try catch
function sum(num1,num2){
    if(typeof num1!=='number') throw new Error('the first parameter must be a number at sum.');
    if(typeof num2!=='number') throw new Error('the second parameter must be a number at sum.');
    return num1 + num2;
}
try{
    console.log(sum(6,5));
} catch(error){
    console.log('O/ops! There is an error', error);
}