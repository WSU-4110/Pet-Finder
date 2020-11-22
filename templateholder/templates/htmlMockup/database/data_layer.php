<?php
   /*$server = "localhost";
   $userName = 
   $pass = 
   $db = */
   
function get_profile_info() {
    global $server, $userName, $pass, $db;
       
    $con=mysqli_connect($server,$userName,$pass,$db);
    if (mysqli_connect_errno()){
        echo "Connection to MySQL unsuccessful: " . mysqli_connect_error();
        die();
    }
    $result = mysqli_query($con,"SELECT * FROM PROFILE;");
    $data=array();
    while($row = mysqli_fetch_array($result)){
        $temp = array();
		array_push($temp,$row['User']);
		array_push($temp,$row['FirstName']);
		array_push($temp,$row['LastName']);
		array_push($temp,$row['Address']);
		array_push($temp,$row['State']);
		array_push($temp,$row['Phone']);
		array_push($temp,$row['AboutMe']);
        array_push($data,$temp);
    }
    mysqli_close($con);
    return $data;
}
 
function update_profile_info($arg_user, $arg_first, $arg_last, $arg_address, $arg_state, $arg_phone, $arg_aboutMe) {
    global $server, $userName, $pass, $db;
       
    $con=mysqli_connect($server,$userName,$pass,$db);
    if (mysqli_connect_errno()){
        echo "Connection to MySQL unsuccessful: " . mysqli_connect_error(); 
        die();
    }
    $stmt = mysqli_prepare($con, "UPDATE PROFILE SET FirstName=?, LastName=?, Address=?, State=?, Phone=?, AboutMe=?  WHERE user=?;");
    mysqli_stmt_bind_param($stmt,"sssssss", $arg_first, $arg_last, $arg_address, $arg_state, $arg_phone, $arg_aboutMe, $arg_user);
    mysqli_stmt_execute($stmt);
    mysqli_close($con);
}
?>