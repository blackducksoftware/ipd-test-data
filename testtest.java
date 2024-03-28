<?php

$username=$_POST['username'];
$password=$_POST['password'];
$sql="SELECT * FROM users WHERE username = :username AND password = :password";

?>```
