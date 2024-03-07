
//FILES WRITING
const fs = require('fs');
const content =" welcome to  Mohamed's familly's house ";

fs.writeFile('./new.txt', content,'utf8', error=>{
    if (error) console.log(error);
    else console.log('file written');
});