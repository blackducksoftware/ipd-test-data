<?php

$username
 
=
 
mysqli_real_escape_string
(
$connection
,
 
$_POST
[
'username'
]
)
;

$password
 
=
 
mysqli_real_escape_string
(
$connection
,
 
$_POST
[
'password'
]
)
;

$sql
 
=
 
"SELECT * FROM users WHERE username = '
$username
' AND password = '
$password
'"
;

?>
