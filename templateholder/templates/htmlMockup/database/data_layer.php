<?php
   /* $server = "localhost";
   $login = 
   $pass = 
   $database = */
   
function get_profile_info() {
    global $server, $login, $pass, $database;
       
    $connection=mysqli_connect($server,$login,$pass,$database);
    if (mysqli_connect_errno()){
        echo "Connection to MySQL unsuccessful: " . mysqli_connect_error();
        die();
    }
    $columns = mysqli_query($connection,"SELECT * FROM PROFILE;");
    $values=array();
    while($row = mysqli_fetch_array($columns)){
        $temp = array();
		array_push($temp,$row['User']);
		array_push($temp,$row['FirstName']);
		array_push($temp,$row['LastName']);
		array_push($temp,$row['Address']);
		array_push($temp,$row['State']);
		array_push($temp,$row['Phone']);
		array_push($temp,$row['AboutMe']);
        array_push($values,$temp);
    }
    mysqli_close($connection);
    return $values;
}
 
function update_profile_info($arg_user, $arg_first, $arg_last, $arg_address, $arg_state, $arg_phone, $arg_aboutMe) {
    global $server, $login, $pass, $database;
       
    $connection=mysqli_connect($server,$login,$pass,$database);
    if (mysqli_connect_errno()){
        echo "Connection to MySQL unsuccessful: " . mysqli_connect_error(); 
        die();
    }
    $statement = mysqli_prepare($connection, "UPDATE PROFILE SET FirstName=?, LastName=?, Address=?, State=?, Phone=?, AboutMe=?  WHERE user=?;");
    mysqli_stmt_bind_param($statement,"sssssss", $arg_first, $arg_last, $arg_address, $arg_state, $arg_phone, $arg_aboutMe, $arg_user);
    mysqli_stmt_execute($statement);
    mysqli_close($connection);
}
?>