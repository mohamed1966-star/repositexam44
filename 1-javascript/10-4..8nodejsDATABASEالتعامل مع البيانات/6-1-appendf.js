
//FILES EDITING append
const fs = require('fs');
const content ="  toto, where are-you?";

fs.appendFile('./new.txt', content,'utf8', error=>{
    if (error) console.log(error);
    else console.log('file written');
})