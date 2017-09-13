<?php
	if(isset($_SESSION['login'])){
		header("location: profile");
	}

	if($_SERVER['REQUEST_METHOD'] === 'POST'){
		$username = htmlspecialchars(filter_var($_POST['username'], FILTER_SANITIZE_STRING));
		$password = htmlspecialchars(filter_var($_POST['password'], FILTER_SANITIZE_STRING));

		if($username && $password){
			$user = $db->querySingle("SELECT * FROM user WHERE username='$username' AND password='$password'", true);
			if($user){
				$data = ['id' => $user['id'], 'username' => $user['username']];
				$_SESSION['login'] = $data;
				header("location: profile");
			}else{
				echo "<script>alert('User does not exist!');</script>";
			}

		}else{
			die("<script>alert('All field must not empty!');window.location.href=window.location.href;</script>");
		}
	}
?>

<section>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-md-6">
      	<div class="p-5">
      		<?php if(isset($_SESSION['register_info'])): ?>
      				<div class="alert alert-success">
      				<?php
      					echo $_SESSION['register_info'];
      					unset($_SESSION['register_info']); 
      				?>
      				</div>
      		<?php endif; ?>
      		<h2>Login</h2><hr/>
	        <form method="POST" class="form">
	        	<div class="form-group">
	        		<input type="text" name="username" class="form-control" placeholder="Username" required>
	        	</div>
	        	<div class="form-group">
	        		<input type="password" name="password" class="form-control" placeholder="Password" required>
	        	</div>
	        	<div class="form-group">
	        		<button type="submit" name="submit" class="btn btn-musicality">Login</button>
	        	</div>
	        </form>
        </div>
      </div>
    </div>
  </div>
</section>