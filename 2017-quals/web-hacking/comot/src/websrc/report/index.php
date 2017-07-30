<?php
session_start();
if (!isset($_SESSION['action'])) {
    $_SESSION['action'] = "0";
}

if(isset($_POST['reporter']) && isset($_POST['url']) && isset($_POST['reason'])){
  $url = $_POST['url'];

  if($_SESSION['action'] > 15){
    die("Kamu melebihi limit!");
  }

  if (!preg_match("/^[A-Za-z0-9]{6}\.html$/i", $url) || !file_exists('../notes/'.$url)) {
    die('url tidak valid.');
  }

  if(!(strpos(file_get_contents("visit_list"), $url) !== false)){
    $file = fopen("visit_list", "a");
    fwrite($file, $_POST['url']."\x0a");
    fclose($file);
    $_SESSION['action'] += 1;
  }

  die('laporan akan di-review oleh admin.');
}

?>

<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Comot - online note service</title>
      <style>
    @import url(https://fonts.googleapis.com/css?family=Merriweather);form,h1{text-align:center}body,form input,form textarea,html{padding:1em;font-family:Merriweather,sans-serif}*,:after,:before{-moz-box-sizing:border-box;-webkit-box-sizing:border-box;box-sizing:border-box}body,html{background:#f1f1f1}h1{color:#a8a8a8;text-shadow:1px 1px 0 #fff}form{max-width:600px;margin:20px auto}form input,form textarea{border:0;outline:0;-moz-border-radius:8px;-webkit-border-radius:8px;border-radius:8px;display:block;width:100%;margin-top:1em;-moz-box-shadow:0 1px 1px rgba(0,0,0,.1);-webkit-box-shadow:0 1px 1px rgba(0,0,0,.1);box-shadow:0 1px 1px rgba(0,0,0,.1);resize:none}form input:focus,form textarea:focus{-moz-box-shadow:0 0 2px #e74c3c!important;-webkit-box-shadow:0 0 2px #e74c3c!important;box-shadow:0 0 2px #e74c3c!important}form #input-submit{color:#fff;background:#e74c3c;cursor:pointer}form #input-submit:hover{-moz-box-shadow:0 1px 1px 1px rgba(170,170,170,.6);-webkit-box-shadow:0 1px 1px 1px rgba(170,170,170,.6);box-shadow:0 1px 1px 1px rgba(170,170,170,.6)}form textarea{height:126px}.half{float:left;width:48%;margin-bottom:1em}.right{width:50%}.left{margin-right:2%}@media (max-width:480px){.half{width:100%;float:none;margin-bottom:0}}.cf:after,.cf:before{content:" ";display:table}.cf:after{clear:both}

    </style>


</head>

<body>

  <h1>Comot Report Page</h1>
<form class="cf" method="POST" action="">
  <div class="half left cf">
    <input name="reporter" type="text" id="input-name" placeholder="Pelapor">
    <input name="url" type="text" id="input-subject" placeholder="xIzs2A.html">
  </div>
  <div class="half right cf">
    <textarea name="reason" type="text" id="input-message" placeholder="Alasan"></textarea>
  </div>

  <input type="submit" value="Submit" id="input-submit">
      <pre>report akan di-review <a href="/admin/" onclick="javascript:event.target.port=30001">admin</a> dalam waktu maksimal 1 jam kedepan</pre>
</form>


</body>
</html>
