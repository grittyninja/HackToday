<?php
$path = 'visit_list';
$url = fgets(fopen($path, 'r'));
$contents = file_get_contents($path);
$contents = str_replace($url, '', $contents);
file_put_contents($path, $contents);
die($url);
?>
