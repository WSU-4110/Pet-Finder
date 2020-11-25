<!doctype html>
<html lang="en">
<head>						<!-- Initialize head content & external links -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pet&ndash;Finder</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="../styles.css">
</head>
<body style="background: #9FE5FF;"> <!-- Body Content -->
    <div class="home-menu pure-menu pure-menu-horizontal pure-menu-fixed">
        <a class="pure-menu-heading" href="index.html">Pet Finder</a>
        <ul class="pure-menu-list"> <!-- Links to other pages -->
            <li class="pure-menu-item"><a href="../index.html" class="pure-menu-link"><b>Home</b></a></li>
            <li class="pure-menu-item"><a href="../questionnaire.html" class="pure-menu-link"><b>Questionnaire</b></a></li>
			<li class="pure-menu-item"><a href="../browse.html" class="pure-menu-link"><b>Browse</b></a></li>
            <li class="pure-menu-item"><a href="../signup.html" class="pure-menu-link"><b>Sign Up</b></a></li>
			<li class="pure-menu-item"><a href="../signin.html" class="pure-menu-link"><b>Sign In</b></a></li>
			<li class="pure-menu-item"><a href="../profile.php" class="pure-menu-link"><i class="fa fa-user-circle"></i><b> My Profile</b></a></li>
        </ul>
    </div><br><br><br>
	<div class="is-center">
		<?php
			$trait = $_GET['trait'];
			$zip = $_GET['zip'];
			$pet = $_GET['animal'];
			$rooms = $_GET['rooms'];
			echo "<h2><b>" . "Entered Zip Code: " . "</b></h2><br>";
			echo '<div style="background-color: white; width: 10%; margin-left: auto; margin-right: auto;">' . "<h3>" . $zip . "</h3></div>" . "<br>";
			echo "<h2><b>" . "Selected Animal: " . "</b></h2><br>";
			echo '<div style="background-color: white; width: 10%; margin-left: auto; margin-right: auto;">' . "<h3>" . $pet . "</h3></div>" . "<br>";
			echo "<h2><b>" . "Number of Rooms Entered: " . "</b></h2><br>";
			echo '<div style="background-color: white; width: 10%; margin-left: auto; margin-right: auto;">' . "<h3>" . $rooms . "</h3></div>" . "<br>";
			echo "<h2><b>" . "Selected Pet Personalities: " . "</b></h2><br>";
			foreach ($trait as $personality){ 
			echo '<div style="background-color: white; width: 10%; margin-left: auto; margin-right: auto;">' . "<h3>" . $personality . "</h3></div>";
			}
			echo "<br><br><br>";
		?>
	</div>
	<div class="footer l-box is-center">
		CSC 4110/1 Group Project - Pet Finder
	</div>
</body>
</html>