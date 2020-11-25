<?php
    require_once "database/data_layer.php";
    function display_table() {        
		$result = get_profile_info();
			foreach ($result as $row) {
				echo "<tr>" . "<td>" . "<h2><b>Username: </b></h2>" . '<div style="margin-left: auto; margin-right: auto;">' . "<h3>" .$row[0] . "</h3>" . '</div>' . "</td>" . "</tr>";
				echo "<tr>" . "<td>" . "<h2><b>First Name: </b></h2>" . '<div style="margin-left: auto; margin-right: auto;">' . "<h3>" .$row[1] . "</h3>" . '</div>' . "</td>" . "</tr>";
				echo "<tr>" . "<td>" . "<h2><b>Last Name: </b></h2>" . '<div style="margin-left: auto; margin-right: auto;">' . "<h3>" .$row[2] . "</h3>" . '</div>' . "</td>" . "</tr>";
				echo "<tr>" . "<td>" . "<h2><b>Address: </b></h2>" . '<div style="margin-left: auto; margin-right: auto;">' . "<h3>" .$row[3] . "</h3>" . '</div>' . "</td>" . "</tr>";
				echo "<tr>" . "<td>" . "<h2><b>State: </b></h2>" . '<div style="margin-left: auto; margin-right: auto;">' . "<h3>" .$row[4] . "</h3>" . '</div>' . "</td>" . "</tr>";
				echo "<tr>" . "<td>" . "<h2><b>Phone: </b></h2>" . '<div style="margin-left: auto; margin-right: auto;">' . "<h3>" .$row[5] . "</h3>" . '</div>' . "</td>" . "</tr>";
				echo "<tr>" . "<td>" . "<h2><b>About Me: </b></h2>" . '<h3 style="word-wrap: break-word; background-color: white; width: 35%; height:20%; margin-left: auto; margin-right: auto;">' .$row[6] . "</h3>" . "<br><br><br>" . "</td>" . "</tr>";
        }
    }
?>
<!doctype html>
<html lang="en">
<head>						<!-- Initialize head content & external links -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Profile</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="styles.css">
</head>
<body style="background: #9FE5FF;"> <!-- Body Content -->
    <div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
        <a class="pure-menu-heading" href="index.html">Pet Finder</a>
		<ul class="pure-menu-list"> <!-- Links to other pages -->
			<li class="pure-menu-item"><a href="index.html" class="pure-menu-link"><b>Home</b></a></li>
			<li class="pure-menu-item"><a href="questionnaire.html" class="pure-menu-link"><b>Questionnaire</b></a></li>
			<li class="pure-menu-item"><a href="browse.html" class="pure-menu-link"><b>Browse</b></a></li>
			<li class="pure-menu-item"><a href="signup.html" class="pure-menu-link"><b>Sign Up</b></a></li>
			<li class="pure-menu-item"><a href="signin.html" class="pure-menu-link"><b>Sign In</b></a></li>
			<li class="pure-menu-item"><a href="profile.php" class="pure-menu-link"><i class="fa fa-user-circle"></i><b> My Profile</b></a></li>
		</ul>
    </div>
									<!-- Profile Pic -->
    <div><a><img src="images/flower.jpg" style="position: absolute; margin-top: 5%; margin-left: 5%;"></a></div>
	<div class="is-center"> <!-- Profile Content -->
		<br><br><h1><b><i class="fa fa-user-circle"></i> My Profile</b></h1>
		<button class="pure-button"><a href="updateProfile.html" style="text-decoration: none; color: white;">Edit</a></button>
		<table style="margin-left: auto; margin-right: auto;">
            <?php
                display_table();
            ?>
        </table>
    </div>

    <div class="footer l-box is-center">
        CSC 4110/1 Group Project - Pet Finder
    </div>

</div>

</body>
</html>