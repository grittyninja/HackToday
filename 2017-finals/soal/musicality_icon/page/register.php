<?php
	function user_exist($username, $db){
		return $db->querySingle("SELECT * FROM user WHERE username='$username'");
	}

	if(isset($_SESSION['login'])){
		header("location: profile");
	}

	if($_SERVER['REQUEST_METHOD'] === 'POST'){
		$username = htmlspecialchars(filter_var($_POST['username'], FILTER_SANITIZE_STRING));
		$password = htmlspecialchars(filter_var($_POST['password'], FILTER_SANITIZE_STRING));

		if($username && $password){
			if(!user_exist($username, $db)){
				$sql = "INSERT INTO user (username, password) VALUES ('$username', '$password')";
				if($db->exec($sql)){
					$_SESSION['register_info'] = "Register success, now you can login";
					header("location: login");
				}
			}else{
				die("<script>alert('Username already exist');window.location.href=window.location.href;</script>");
			}
		}else{
			die("<script>alert('All field must not empty');window.location.href=window.location.href;</script>");
		}
	}
?>

<section>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-md-6">
      	<div class="p-5">
      		<h2>Register</h2><hr/>
	        <form method="POST" class="form">
	        	<div class="form-group">
	        		<input type="text" name="username" class="form-control" placeholder="Username" required>
	        	</div>
	        	<div class="form-group">
	        		<input type="password" name="password" class="form-control" placeholder="Password" required>
	        	</div>
	        	<div class="form-group">
	        		<button type="submit" name="submit" class="btn btn-musicality">Register</button>
	        	</div>
	        </form>
        </div>
      </div>
    </div>
  </div>
</section>