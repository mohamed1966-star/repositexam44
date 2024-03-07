const fs = require('fs');

fs.readFile('messages.txt', 'utf-8', (error, data) => {
    if(error) console.log(error);
    else{
        const messages = data.split(',');
        console.log(messages);
    } 
});

console.log("Executed after read file");

