const fs = require('fs');

fs.readFile('messages.txt', 'utf-8', (error, data) => {
    if(error) console.log(error);
    else console.log(data); 
});

