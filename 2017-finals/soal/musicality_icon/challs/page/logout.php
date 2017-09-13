<?php
if($_SERVER['REQUEST_METHOD'] === 'POST'){
	if(isset($_SESSION['login'])){
		unset($_SESSION['login']);
		session_destroy();
	}
}