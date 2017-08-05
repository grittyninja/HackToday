<html>
<head></head>
<body>
	<form action="" method="POST">
		Password : <input type="text" name="password">
		<input type="submit" name="submit">
	</form>
</body>
</html>



<?php

$flag ="HackToday{t111111me3e3e3e3e3e3e_15555_moneyyy_artinya_____waktu_adal777777aaaahhhh____uang__$$$$$$$$}";
if(isset($_POST['password']))
{
	for($i = 0; $i < strlen($flag); $i++)
	{
		if($_POST['password'][$i] == $flag[$i])
			sleep(1);
		else
			die("Wrong!");
	}
}
?>
