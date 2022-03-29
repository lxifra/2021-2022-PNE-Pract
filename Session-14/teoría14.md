module: we have to put them in the file where we are working.

<!DOCTYPE html>
<html lang="en">
<head>   #to create a tag
    <meta charset="UTF-8">
    <title>Pink</title>  #the browser will reveal the content of the title in the page (at the top of it).
</head>
<body style="background-color: pink;">
  <h1>Pink</h1>
  <p>This is the pink page</p>
  <a href="/">Main page</a>
</body>
</html>


En la terminal:
python.exe -m http.server 8080

Para entrar a las páginas por google:
localhost:8080

Lo único que puede ofrecerte el http es un file que le preguntas, pero para llegar a él se necesitan
otros protocolos ( o algo así ) como el TCP.