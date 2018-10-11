<?php
$servername = "localhost";
$username = "user";
$password = "Zn4xqAO23Xs9jj1J";
$DBname = "my_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $DBname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
// echo "Connected successfully";

?>
