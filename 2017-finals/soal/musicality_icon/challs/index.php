<?php

require_once(__DIR__.'/config/dbconnection.php');
session_start();

?>

<?php
	$islogin = false;
	if(isset($_SESSION['login'])){
		$islogin = true;
	}
?>

<!DOCTYPE html>
<html lang="en">

  <head>
  	
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <?php include "content/head.php"; ?>
  </head>

  <body>
  	<?php
  		include "content/header.php"; 
  		if(isset($_GET['p'])){
  			$page = $_GET['p'];
  			if(include "page/$page.php");
  			else header("location: 404");
  		}else{
  			include "page/home.php";
  		}
  		include "content/footer.php";
  	?>
  
  </body>

</html>