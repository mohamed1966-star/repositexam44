function hello1(){
    console.log('Hello World');
}
hello1();
console.log('---------------------------------------------');
//
function hello(){
    const name = 'hassoub';
    console.log('Hello '+name);
}
hello();
console.log('---------------------------------------------');
//
function filterArray(){
    const array =['Ahmed',1,'Sami','Momo',258];
    for(let item of array){
        if(typeof item ==='string')
        console.log(item);
    }
}
filterArray();