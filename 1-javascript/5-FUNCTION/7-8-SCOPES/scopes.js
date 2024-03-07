//GLOBAL SCOPE
const msg = 'Hassoub';
console.log(msg);
console.log('-------------------------------------------');
//LOCAL SCOPE
const msg1  = 'JAMAL';
function hello(){
    
    console.log(msg1);
}
hello();
console.log('-------------------------------------------');
//GLOBAL SCOPE
function hello(){
    //LOCAL SCOPE
    const msg= 'Hassoub';
    console.log(msg);
}
function bye(){
    //LOCAL SCOPE
    const msg = 'Bye';
    console.log(msg);
}
//hello();
bye();