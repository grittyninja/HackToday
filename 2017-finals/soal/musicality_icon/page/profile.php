<?php
	if(!isset($_SESSION['login'])){
		header("location: login");
	}

	function sanitize_input($data){
		return htmlspecialchars(filter_var($data, FILTER_SANITIZE_STRING));
	}

	function random($length = 10){
		$characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
	}

	function curl_img($url){

		$get_img = curl_init($url);
		// curl_setopt ($get_img, CURLOPT_URL, $img_url);

		curl_setopt($get_img, CURLOPT_HEADER, 0);
		curl_setopt($get_img, CURLOPT_RETURNTRANSFER, 1);
		curl_setopt($get_img, CURLOPT_BINARYTRANSFER, 1);
	  curl_setopt($get_img, CURLOPT_CAINFO, __DIR__.'/../config/cacert.pem');

		$raw_img = curl_exec($get_img);
		curl_close($get_img);

		$random_text = time().random();
		$save_img = __DIR__.'/../static/img/'.md5($random_text);
		$save_img .= ".jpg";

		$fp = fopen($save_img, 'w') or die("Unable to open file");
		fwrite($fp, $raw_img);
		fclose($fp);

		$location = 'static/img/'.md5($random_text).'.jpg';
		return $location;
	}

	$usid = $_SESSION['login']['id'];
	$user = $db->querySingle("SELECT * FROM user WHERE id=$usid", true);

	if($_SERVER['REQUEST_METHOD'] === 'POST'){
		$data = $_POST;
		foreach($data as $key => $d){
			$filter = ['submit', 'avatar'];
			if(!in_array($key, $filter) && !$d){
				die("<script>alert('all field must not empty');window.location.href=window.location.href;</script>");
			}
		}
		if($data['avatar']){
			$img = curl_img($data['avatar']);
			$sql = "UPDATE user SET fullname='".sanitize_input($data["fullname"])."', birthdate='".sanitize_input($data["birthdate"])."', address='".sanitize_input($data["address"])."', avatar='$img' WHERE id=$usid";
		}else{
			$sql = "UPDATE user SET fullname='".sanitize_input($data["fullname"])."', birthdate='".sanitize_input($data["birthdate"])."', address='".sanitize_input($data["address"])."' WHERE id=$usid";
		}
		if($db->exec($sql)){
			$_SESSION['update_info'] = "Success updating profile";
			die("<script>window.location.href=window.location.href</script>");
		}else{
			echo "<script>alert('Updating profile failed');</script>";
		}
	}
?>

<section>
  <div class="container">
    <div class="row align-items-center">
      <div class="col-md-12">
      	<div class="p-5">
      		<h2>&nbsp;My Profile</h2>
      		<?php if(isset($_SESSION['update_info'])): ?>
      				<div class="alert alert-success">
      					<?php 
      						echo $_SESSION['update_info'];
      						unset($_SESSION['update_info']);
      					?>
      				</div>
      		<?php endif; ?>
					<ul class="nav nav-tabs" role="tablist">
					  <li class="nav-item">
					    <a class="nav-link active" data-toggle="tab" href="#profile" role="tab">Profile</a>
					  </li>
					  <li class="nav-item">
					    <a class="nav-link" data-toggle="tab" href="#upload" role="tab">Upload Music</a>
					  </li>
					  <li class="nav-item">
					    <a class="nav-link" data-toggle="tab" href="#settings" role="tab">Settings</a>
					  </li>
					</ul>

					<!-- Tab panes -->
					<div class="tab-content">
					  <div class="tab-pane active" id="profile" role="tabpanel">
				  		<h4 style="padding-top:20px;padding-bottom:10px">My profile information</h4>
					  	<div class="row" style="padding: 0 20px">
					  		<div class="col-md-2" style="border: 1px solid #ccc;border-radius: 15px;">
					  			<center>
					  			<img src="<?php echo $user['avatar']?$user['avatar']:'static/img/default_avatar.png'; ?>" style="max-width: 70%">
					  			</center>
					  		</div>
						 		<div class="col-md-10">
							  	<table>
							  		<tr>
							  			<td>Full Name</td>
							  			<td>: </td>
							  			<td><?php echo $user['fullname']?$user['fullname']:'-' ?></td>
							  		</tr>
							  		<tr>
							  			<td>Birthdate</td>
							  			<td>: </td>
							  			<td><?php echo $user['birthdate']?$user['birthdate']:'-' ?></td>
							  		</tr>
							  		<tr>
							  			<td>Address</td>
							  			<td>: </td>
							  			<td><?php echo $user['address']?$user['address']:'-' ?></td>
							  		</tr>
							  	</table>
							  </div>
							</div>
					  </div>
					  <div class="tab-pane" id="upload" role="tabpanel"><h4 style="padding-top:20px;padding-bottom:10px">Upload your music here</h4><p>TO DO</p></div>
					  <div class="tab-pane" id="settings" role="tabpanel">
					  	<h4 style="padding-top:20px;padding-bottom:10px">Edit your profile information</h4>
					  	<div class="row" style="padding: 0 20px">
					  		<div class="col-md-12">
						  		<form method="POST" class="form form-horizontal">
						  			<div class="form-group">
						  				<label for="fullname">Fullname</label>
						  				<input type="text" name="fullname" value="<?php echo $user['fullname'] ?>" placeholder="Your Fullname" class="form-control" required/>
						  			</div>
						  			<div class="form-group">
						  				<label for="birthdate">Birthdate</label>
						  				<input type="text" name="birthdate" id="bd" value="<?php echo $user['birthdate'] ?>" placeholder="Your Birthdate (dd/mm/yyyy)" class="form-control" required/>
						  			</div>
						  			<div class="form-group">
						  				<label for="address">Address</label>
						  				<input type="text" name="address" value="<?php echo $user['address'] ?>" placeholder="Your Address" class="form-control" required/>
						  			</div>
						  			<div class="form-group">
						  				<label for="avatar">Avatar URL</label>
						  				<input type="text" name="avatar" placeholder="Your Avatar URL (http://example.com/avatar.jpg)" class="form-control"/>
						  			</div>
						  			<div class="form-group">
						  				<button type="submit" name="submit" class="btn btn-musicality">Save</button>
						  			</div>
						  		</form>
					  		</div>
					  	</div>
					  </div>
					</div>
        </div>
      </div>
    </div>
  </div>
</section>