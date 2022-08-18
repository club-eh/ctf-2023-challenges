<!DOCTYPE html>
<html lang="en">
<head>
    <!-- CDNs -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js"></script>

    <!-- CSS -->
    <link rel="stylesheet" href="./style.css">

    <!-- meta -->
    <title>Olympians</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<!-- content  -->
<body>
	<!-- navigation bar-->
	<nav class="navbar-expand navbar-light nav-style fixed-top">
	    <a class="navbar-brand m-2" href="#">Olympians</a>
	</nav>
    <div class="container content">
        <!-- search form-->
        <div>
            <form class="search-style p-2" method="post">
				<input type="text" name="search" placeholder="Search Query" required>
               	<button type="submit" class="btn btn-primary">
                   	<i class="fa fa-search"></i>
				</button>
			</form>	
		</div>
		<!-- search results -->
        <div class="row"> 
			<?php
				require "search.php";
				if (isset($_POST["search"])) {
					search();
				}
			?>
		</div>	
    </div>

	<!-- footer -->
	<footer class="nav-style text-center footer fixed-bottom">
    	<div>
        	2023 Club.eh
		</div>
	</footer>
</body>
</html>
