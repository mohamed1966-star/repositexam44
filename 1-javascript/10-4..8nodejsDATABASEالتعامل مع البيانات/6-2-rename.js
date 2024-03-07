//FILES RENAME
const fs = require('fs');
const content = "Welcome to Mohamed's house" 
fs.rename('./messages.txt', 'msgs.txt', error => {
    if(error) console.log(error);
    else{
        console.log('Renamed');
    } 
});
