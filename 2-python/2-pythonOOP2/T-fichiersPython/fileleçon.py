f = open('learn.txt', 'w')
f.write('lets learn python whith me\n')
f.write('siiiiir lbher avec..........')
f.close()

R = open('indexh.html', 'w')
html='''
<html>
    <head>
        <title>HTML with Python</title>
        <link rel='stylesheet' href='indexC.css'>
        <script src='indexJ.js'></script
    </head>
    <body>
        <center> <h2>Learn Python by myself <h2/>
        <hr>
        <h3 id='para'> PYTHON 2023</h3>
        </center>
    </body>
</html>
'''
R.write(html)
R.close

C = open('indexC.css', 'w')
css ='''
body {
    background-color:black;
}
h2 {
    color:red;
}
h3{
    color:yellow;
}
'''
C.write(css)
C.close()

J = open('indexJ.js', 'w')
js ='''
alert('Welcome to our site');
function ok():
    
'''
J.write(js)
J.close()