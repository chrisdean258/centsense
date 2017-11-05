<?php

session_cache_limiter('none');
session_start();

show_header();

switch($_REQUEST['func']) {
	case "login":
		verify_login();
		break;
	case "add":
		show_page();
		break;	
	default:
		show_login();
		break;
}


function show_header() {
	?>
		<!DOCTYPE html>
		<link rel='stylesheet' href='css/style.css' type='text/css' media='all' />
		<html>
		<head>

		<meta charset="UTF-8">

		<title>Cent Sense</title>

		<link rel="shortcut icon" type="ico/ico" href="http://ec2-18-221-85-87.us-east-2.compute.amazonaws.com/favicon.ico" />
		<style>
		@import url(http://fonts.googleapis.com/css?family=Exo:100,200,400);
	@import url(http://fonts.googleapis.com/css?family=Source+Sans+Pro:700,400,300);

	body{
margin: 0;
padding: 0;
background: #fff;

color: #fff;
       font-family: Arial;
       font-size: 12px;
	}

	.body{
position: absolute;
top: -20px;
left: -20px;
right: -40px;
bottom: -40px;
width: auto;
height: auto;
	background-image: url(https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQiDYixL9yLGIraKVCWlOqaaG5jmREeG5HRhRRAqw8bNp-7wz8);
	background-size: cover;
	-webkit-filter: blur(5px);
	z-index: 0;
	}

	.grad{
position: absolute;
top: -20px;
left: -20px;
right: -40px;
bottom: -40px;
width: auto;
height: auto;
background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,rgba(0,0,0,0)), color-stop(100%,rgba(0,0,0,0.65))); /* Chrome,Safari4+ */
	    z-index: 1;
opacity: 0.7;
	}

	.header{
position: absolute;
top: calc(50% - 35px);
left: calc(50% - 255px);
      z-index: 2;
	}

	.header div{
float: left;
color: #fff;
       font-family: 'Exo', sans-serif;
       font-size: 35px;
       font-weight: 200;
	}

	.header div span{
		font-weight:bold;
color: #89cff0 !important; <!--#5379fa--><!--UT Orange FF8200--><!--Torch E65933-->
	}

	.login{
position: absolute;
top: calc(50% - 75px);
left: calc(50% - 50px);
height: 10px;
width: 10px;
padding: 10px;
	 z-index: 2;
	}

	.login input[type=text]{
width: 250px;
height: 30px;
background: transparent;
border: 1px solid rgba(255,255,255,0.6);
	border-radius: 2px;
color: #fff;
       font-family: 'Exo', sans-serif;
       font-size: 16px;
       font-weight: 400;
padding: 4px;
	}

	.login input[type=password]{
width: 250px;
height: 30px;
background: transparent;
border: 1px solid rgba(255,255,255,0.6);
	border-radius: 2px;
color: #fff;
       font-family: 'Exo', sans-serif;
       font-size: 16px;
       font-weight: 400;
padding: 4px;
	 margin-top: 10px;
	}

	.login input[type=button]{
width: 260px;
height: 35px;
background: #fff;
border: 1px solid #fff;
cursor: pointer;
	border-radius: 2px;
color: #a18d6c;
       font-family: 'Exo', sans-serif;
       font-size: 16px;
       font-weight: 400;
padding: 6px;
	 margin-top: 10px;
	}

	.login input[type=button]:hover{
opacity: 0.8;
	}

	.login input[type=button]:active{
opacity: 0.6;
	}

	.login input[type=text]:focus{
outline: none;
border: 1px solid rgba(255,255,255,0.9);
	}

	.login input[type=password]:focus{
outline: none;
border: 1px solid rgba(255,255,255,0.9);
	}

	.login input[type=button]:focus{
outline: none;
	}

	::-webkit-input-placeholder{
color: rgba(255,255,255,0.6);
	}

	::-moz-input-placeholder{
color: rgba(255,255,255,0.6);
	}

	input[type=checkbox] {
visibility: hidden;
	}
	</style>

		<script src="js/prefixfree.min.js"></script>

		</head>
		</html>
		<?php
}

function show_login($error, $title) {
	?>


		<body>

		<div class="body"></div>
		<div class="grad"></div>
		<div class="header">
		<div>CENT<span>Sense</span></div><P>
		</div>
		<br>
		<div class="login">

		<div align="center"><b><?php echo $error?></b>
		</div>
		<form name="login_form" method="post" action="<?php echo $url?>"><br />
		<table width="250" border="0" style="border-collapse:collapse; margin: auto;">
		<tr>
		<td><label for='netid'>Username:</td>
		<td width="10">&nbsp;</td>
		<td><input type="text" name="netid" id='netid' maxlength="15" class="form-control" placeholder="Username" /></td>
		</tr>
		<tr>
		<td><label for='password'>Password:</label></td>
		<td width="10">&nbsp;</td>
		<td><input type="password" name="password" id='password' class='form-control' placeholder="Password"/>
		<input type="hidden" name="func" value="login" />
		</td>
		</tr>
		<tr>
		<td colspan="3" height="40" align="center">
		<input type="submit" name="Login" value="Login" class="button1" />
		<input type="reset" name="Reset" value="Reset" class="button1" />
		</td>
		</tr>
		</table>
		</form>







		</div>

		</body>

		<?php
}


function show_page() {
	?>

		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

		<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
		<script>
		$(function () {
				$('button').click(function () {
						var name2 = $('#name').val();
						var email2 = $('#email').val();
						var password2 = $('#password').val();
						var gender2 = $('#gender').val();
						console.log('starting ajax');
						$.ajax({
url: "./insert.php",
type: "post",
data: { name: name2, email: email2, password: password2, gender: gender2 },
success: function (data) {
var dataParsed = JSON.parse(data);
console.log(dataParsed);
}
});

						});
				});

</script>

<script>
function showUser(str) {
	if (str == "") {
		document.getElementById("txtHint").innerHTML = "";
		return;
	} else { 
		if (window.XMLHttpRequest) {
			// code for IE7+, Firefox, Chrome, Opera, Safari
			xmlhttp = new XMLHttpRequest();
		} else {
			// code for IE6, IE5
			xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
		}
		xmlhttp.onreadystatechange = function() {
			if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
				document.getElementById("txtHint").innerHTML = xmlhttp.responseText;
			}
		};
		xmlhttp.open("GET","getuser.php?q="+str,true);
		xmlhttp.send();
	}
}


</script>

<style>
.custom{
	margin-left:200px;
}

.center_div{
margin: 0 auto;
padding: 40px;
}

</style>
</head>
<body>

<br/>
<center><img src="imgs/oit_banner_ethernet.gif" alt="Ethernet Banner" style="width:960px;height:;"></center>
<br/>
<br/>
<br/>

<div class="container">

<h2 class="text-center">OIT Ethernet</h2>
<div class="row">
<form class="form-horizontal" >

<div class="form-group">
<label class="col-sm-offset-3 col-sm-2 control-label">NetID</label>
<div class="col-sm-3">
<input class="form-control" name="name" id="name" type="text" placeholder="Enter their netid" onkeyup="showUser(this.value)">
</div>
</div>

<center><div id="txtHint"><b>Enter the users netid, and their history is below:</b></div></center><br/>

<div class="form-group">
<label for="gender" class="col-sm-offset-3 col-sm-2 control-label">Cable Length</label>
<div class="col-sm-3">
<select id="gender" class="form-control">
<option value="14ft">14ft</option>
<option value="25ft">25ft</option>
</select>
</div>
</div>

<div class="form-group">
<div class="col-sm-offset-4 col-sm-3">
<form action="" method="post">
<input type="hidden" name="func" value="add" />
<button type="submit" class="btn btn-default" value='add'>Submit</button>
</form>
</div>
</div>
</form>
</div>
</div>

</body>

<?php
}
?>


