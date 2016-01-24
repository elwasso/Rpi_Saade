<!DOCTYPE HTML>
<html>
	<head>
		<title>My Home</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1,user-scalable=no" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<?php include('functions.php'); ?>
	</head>
	<body>


		<!-- Work -->
			<div class="wrapper style2">
				<header>
					
<div id="electstatus">


	<div class="item">
		<img src="img/on.png" width="40" class="off">
		<img src="img/off.png" width="40" class="on">
		EDL
	</div>


	<div class="item">
		<img src="img/on.png" width="40" class="off">
		<img src="img/off.png" width="40" class="on">
		Generator
	</div>
</div>
				</header>
				<article >
					<div class="container">
						<div class="row">


							<div class="6u 12u(mobile)" id="action_section">
								<section class="box ">
									<div class="row">
										<div class="12u">
										<h2>Current Status</h2>

										<h5>Electric Heater</h5>
											<a href="javascript:void(0)" class="button" data-method="5" data-status="1">On</a>
										</div>	

										<div class="12u">
											<h5>Diesel Heater</h5>
											<a href="javascript:void(0)" class="button" data-method="6" data-status="1">On</a>
										</div>	
										<div class="12u">
											<h5>Washing Machine</h5>
											<a href="javascript:void(0)" class="button " data-method="13" data-status="1">On</a>
										</div>	
									</div>
								</section>
							</div>
							<div class="6u 12u(mobile)" id="preset_section">
								<section class="box">
									<div class="row">
										<div class="12u">
										<h2>On EDL (Diesel Heater will work also on Generator)</h2>
										<h5>Electric Heater</h5>
											<a href="javascript:void(0)" class="button preset" data-method="5" data-status="">Keep Off</a>
										</div>	

										<div class="12u">
											<h5>Diesel Heater</h5>
											<a href="javascript:void(0)" class="button preset" data-method="6" data-status="">Keep Off</a>
										</div>	
										<div class="12u">
											<h5>Washing Machine</h5>
											<a href="javascript:void(0)" class="button preset" data-method="13" data-status="">Keep Off</a>
										</div>	
									</div>


								</section>
							</div>
						</div>
					</div>
					<footer>
						<p>&copy; elwasso.com</p>
						
					</footer>
				</article>
			</div>



		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script type="text/javascript" src="script/script.js"></script>
			<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->

	</body>
</html>