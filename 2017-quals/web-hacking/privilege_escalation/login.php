<?php
$myusername = mysqli_real_escape_string($_POST['username']);
$mypassword = mysqli_real_escape_string($_POST['password']); 
echo $myusername;
echo $mypassword;
?>

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

<!-- jQuery library -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>

<!-- Latest compiled JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

<div class="container">
	<h2>Login</h2>
	<br>
	<form method="POST" action="">
    <div class="form-group">
        <label for="username">Username</label>
        <input type="text" placeholder="" class="form-control" id="username" placeholder="Your username" />
    </div>
    <div class="form-group">
        <label for="password">password</label>
        <input type="password" placeholder="" class="form-control" id="password" placeholder="password" />
    </div>
    
        <button class="btn btn-block btn-danger btn-lg">Login</button>
        
     </form>
