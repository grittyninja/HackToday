<?php
putenv("THIS=COBA");
$file = fopen($_GET['param'], "r");
/* Do some operation on the file handler, like maybe read the file and output it */
$contents = fread($file, 400);
print_r($contents);

fclose($file);
print "hii";
?>
