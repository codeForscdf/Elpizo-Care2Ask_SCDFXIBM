
/* This page contains the interface for the public to upload the image they found to a S3 bucket. */

<!DOCTYPE HTML>
		<html>
			<head>
				<title>Facial Comparison</title>
				<meta charset="utf-8" />
				<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
				<link href="https://teamelpizo.github.io/css/solutionsDesign.css" rel="stylesheet" type="text/css" />
				<script src="https://kit.fontawesome.com/a076d05399.js"></script>
				<script type="text/javascript" src="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/js/jquery-3.2.1.min.js"></script>
				<script type="text/javascript" src="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/js/plugins-activate.js"></script>
			<script type="text/javascript" src="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/js/solutions.js"></script>
			<style>
				.chatContain {
					position: relative;
					top: 10px;
					left: 650px;}
			</style>
			</head>

<body class="is-preload"><div id="wrapper">
<nav id="nav"><ul>
<li><a href="#calendar">Happy Sundowning</a></li>
<li><a href="#roster">Family Interface</a></li>
<li><a href="#callSign">Public Interface</a></li>
               </ul></nav>
<a class="menu-toggle rounded"><i class="fa fa-bars"></i></a>
<nav id="sidebar-wrapper"><ul class="sidebar-nav">
	<li class="sidebar-brand"><a class="smooth-scroll" href="#Header"></a></li>
	<li class="sidebar-nav-item"><a href="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/index.html" title="Back to Main Page"> Home </a></li>
	<li class="sidebar-nav-item"><a href="https://drive.google.com/file/d/1vGvRtevon4nomO8PBOOpFbgcUawgHte2/view?usp=sharing" title="Our Ideas">Brainstorm</a></li>
	<li class="sidebar-nav-item"><a href="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/impact.html" title="Goals">Aims and Impact</a></li>
	<li class="sidebar-nav-item"><a href="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/solution.html" title="Summary of our Solutions">Solutions</a></li>
	<li class="sidebar-nav-item"><a href="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/reflections.html" title="Critique of Solution">Reflections</a></li>
	<li class="sidebar-nav-item"><a href="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/aboutus.html" title="Who Are We">About Us</a></li>
																					 </ul></nav>
						<!-- Main -->
<div id="main"><section id="intro" class="main"><div class="spotlight"><div class="content">
<header class="major"><h2>Care2Ask Beta</h2>
<form action="upload.php" method="post" enctype="multipart/form-data">
		Please enter your phone number for us to send the facial comparison results to:
<input type="text" name="phNumber" style="width:100px;"><br/>
<form action="" method="post" enctype="multipart/form-data">
    Select image to upload for Comparison with our database: </br><br/>&nbsp;&nbsp;&nbsp;
<input type="file" name="fileToUpload" id="fileToUpload">&nbsp;
<input type="submit" value="Upload and Compare" name="submit">
</form>
</header><h2><b>

<?php
$target_dir = "";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

if(isset($_POST["submit"])) {
	$check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
	if($check !== false)
	{echo "File is an image - " . $check["mime"] . ".";
	$uploadOk = 1;}
	else {echo "File is not an image.";
	$uploadOk = 0;}}

if (file_exists($target_file))
 {echo "Sorry, file already exists.";
 $uploadOk = 0;}

						if ($_FILES["fileToUpload"]["size"] > 500000) {
						  echo "Sorry, your file is too large.";
						  $uploadOk = 0;
						}

						if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg"
						&& $imageFileType != "gif" ) {
						  echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.";
						  $uploadOk = 0;
						}

						if ($uploadOk == 0) {
						  echo "Sorry, your file was not uploaded.";

						} else {
						  if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
						    echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
						  } else {
						    echo "Sorry, there was an error uploading your file.";
						  }
						}
						?></b></h2>
</div>
</div>
</section>
</div>
<div class="chatContain">
<iframe src="https://codeforscdf.github.io/Elpizo-Care2Ask_SCDFXIBM/pages/solution/askopweb.html" title="Chatbot" width="350" height="400"></iframe>
</div>
</div>
					</section>

</body>
</html>
