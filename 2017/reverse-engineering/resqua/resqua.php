<?php

$FLAG = "HackToday{perfect_square_is_perfect}";

// =====================================================================

function c($n)
{
  if ($n < 1111) return false;
  $i = 1;
  while ($n > 0) {
    $n -= $i;
    $i += 2;
  }
  return $n == 0;	
}

if (isset($_GET['serial'])) {

	$serial = $_GET['serial'];

	if (! (strlen($serial) == 19 && $serial[4] == '-' && $serial[9] == '-' && $serial[14] == '-')) {
		die("Wrong format");
	} else {
		for ($i = 0; $i < 20; $i++) {
			if (isset($serial[$i]) && $serial[$i] == '0') {
				die("Invalid serial number");
			}
		}
		
		$parts = explode("-", $serial);
		$part1 = intval($parts[0]);
		$part2 = intval($parts[1]);
		$part3 = intval($parts[2]);
		$part4 = intval($parts[3]);
		
		if (c($part1) && c($part2) && c($part3) && c($part4) && ($part1 < $part2 && $part2 < $part3 && $part3 < $part4)) {
			echo "<h1>GRATE!</h1>";
			echo "<p>$FLAG</p>";
			die();
		} else {
			die("Invalid serial number");
		}		
		
	}

}

?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
	<title>ReSqua</title>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
</head>

<body>
	<form action="" method="get">
		<p>Enter something: </p>
		<input type="text" name="serial" size="40">
	</form>
</body>

</html>
