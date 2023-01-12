<?php
	include 'src/setCookies.php';
?>
<!DOCTYPE HTML>
<head>
	<script src="./lib/bootstrap.bundle.min.js"></script>
	<link href="./lib/bootstrap.min.css" rel="stylesheet">
	<script src="./lib/jquery.min.js"></script>
	<link href="./style.css" rel="stylesheet">
	<script src="src/popoverFunc.js"></script>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
	<nav class="navbar" style="background-color: #315527;">
		<div class="container-fluid">
    		<span class="navbar-brand mb-0 h1" style="color: #000000">Botanic Market</span>
		</div>
	</nav>
	<div class="container">
		<div class="row">
			<div class="col-3">
				<img class="sign" src="img/sign.png"></img>
			</div>
			<div class="col-6 pt-3 text-center">
				<img class="banner" src="img/banner.png"></img>
			</div>
		</div>
		<hr style="color: #FFFFFF;">

		<?php
			include 'src/checkRole.php';
		?>
	
		<hr style="color: #FFFFFF;">
		<div class="row text-center" style="height: fit-content; width: fit-content;">
			<div class="col-3 item">
				<img class="picture" src="img/1.png" data-toggle="chestnut"></img>
				<p>Horse Chestnut Seedling</p>
				<p>$8.99</p>
			</div>
			<div class="col-3 item">
				<img class="picture" src="img/2.png" data-toggle="maple"></img>
				<p>Maple Seedling</p>
				<p>19.99</p>
			</div>
			<div class="col-3 item">
				<img class="picture" src="img/3.png" data-toggle="poplar"></img>
				<p>Poplar Seedling</p>
				<p>$1.99</p>
			</div>
			<div class="col-3 item">
				<img class="picture" src="img/4.png" data-toggle="willow"></img>
				<p>Willow Seedling</p>
				<p>$12.99</p>
			</div>
		</div>
		<div class="row text-center g-5">
			<div class="col-3">
				<img class="picture" src="img/5.png" data-toggle="alder"></img>
				<p>Red Alder Seedling</p>
				<p>$2.99</p>
			</div>
			<div class="col-3">
				<img class="picture" src="img/6.png" data-toggle="clover"></img>
				<p>Clover</p>
				<p>$22.99</p>
			</div>
			<div class="col-3">
				<img class="picture" src="img/sentient.png" data-toggle="sentient"></img>
				<p>Sentient plant</p>
				<p style="color: #FF0000">OUT OF STOCK</p>
			</div>
			<div class="col-3">
				<img class="picture" src="img/8.png" data-toggle="oak"></img>
				<p>Oak Seedling</p>
				<p>$6.99</p>
			</div>
		</div>

</div>
</body>
