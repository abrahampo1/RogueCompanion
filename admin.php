<?php
$servername = "localhost";
$database = "rogue";
$username = "root";
$password = "";
// Create connection
$link = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$link) {
      die("Connection failed: " . mysqli_connect_error());
}

if(isset($_POST["api"])){
      $api = $_POST["api"];
      $sql = "SELECT * FROM ordenadores WHERE BINARY api = '$api' and admin = 1";
      if($do = mysqli_query($link, $sql)){
            if($do->num_rows > 0){

            }else{
                  echo "<video src='https://ir.stonybrook.edu/xmlui/bitstream/handle/11401/9656/rickroll.mp4?sequence=1' autoplay>";
            }
      }
}

?>

<form action="" method="post">
<input type="text" name="api" placeholder="api">
<button>Enviar</button>
</form>