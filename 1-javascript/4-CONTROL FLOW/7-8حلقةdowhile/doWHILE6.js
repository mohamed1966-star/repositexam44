// do while
let i = 1;
do {
    if (i % 2 === 0) console.log(i);
    i++;
} while (i <= 10);

console.log('---------------------------------------------------')
// مصفوفات FOR
const names = ['Ahmed', 'Ibrahim', 'AbdAllah', 'Omar'];

for (let i = 0; i < names.length; i++) {
    console.log(i, names[i]);
    
}console.log(names.length)

console.log('---------------------------------------------------')
// صفوفات WHILE
let x = 0;
while (x <  names.length ){
    console.log(x,names[x]);
    x++;
}

console.log('---------------------------------------------------')
// contraire
for(let i = names.length -1;i>=0; i--){
    console.log(i,names[i]);
}

console.log('---------------------------------------------------')
let x1 = names.length -1;
while (x1 >= 0 ){
   console.log(x1,names[x1]);
    x1--;
}

console.log('---------------------------------------------------')

