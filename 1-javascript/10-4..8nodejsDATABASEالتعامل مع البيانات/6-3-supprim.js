//FILES deleted
const fs = require('fs');
const content = "Welcome to Mohamed's house" 
fs.unlink('./msgs.txt', error => {
    if(error) console.log(error);
    else{
        console.log('Deleted');
    } 
});
