<?php
    require_once "data_layer.php";
    if($_POST) {
        if(isset($_POST['user']) && isset($_POST['firstChange']) && isset($_POST['lastChange']) && isset($_POST['addressChange']) && isset($_POST['stateChange']) && isset($_POST['phoneChange']) && isset($_POST['aboutMeChange'])) {
			$user = htmlspecialchars($_POST['user']);
			$firstName = htmlspecialchars($_POST['firstChange']);
			$lastName = htmlspecialchars($_POST['lastChange']);
			$address = htmlspecialchars($_POST['addressChange']);
			$state = htmlspecialchars($_POST['stateChange']);
			$phoneNum = htmlspecialchars($_POST['phoneChange']);
			$about = htmlspecialchars($_POST['aboutMeChange']);
            update_profile_info($user, $firstName, $lastName, $address, $state, $phoneNum, $about);
            header("location: ../profile.php");
        }
    }
?>