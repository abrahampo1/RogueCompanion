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
                  ?>
                  
                  
                  <body>
                        <div class="titulo"><h1>EL ADMIN</h1></div>
                        <div class="ordenadores">
                        
                              <?php
                              
                              $sql = "SELECT * FROM ordenadores WHERE whitelist = 0";
                              $do = mysqli_query($link, $sql);
                              while($pc =  mysqli_fetch_assoc($do)){
                                    ?>
                                    
                                    <div class="ordenador">
                                          <h2><?php echo $pc["nombre_custom"] ?></h2>
                                          <h3><?php echo $pc["ip"] ?></h3>
                                          <h4><?php echo $pc["hostname"] ?></h4>
                                    </div>
                                    
                                    <?php
                              }
                              
                              ?>

                        </div>
                  </body>
                  
                  
                  
                  
                  <?php
            }else{
                  echo "<video src='https://ir.stonybrook.edu/xmlui/bitstream/handle/11401/9656/rickroll.mp4?sequence=1' autoplay controls>";
            }
      }
}

?>

<form action="" method="post">
<input type="text" name="api" placeholder="api">
<button>Enviar</button>
</form>



<style>
      .ordenadores{
            display: flex;
            flex-wrap: wrap;
      }

      .ordenador{
            margin: 20px;
      }
</style>