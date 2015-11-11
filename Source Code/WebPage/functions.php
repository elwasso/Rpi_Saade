<?php

$method = $_POST['method'];
$status = (string)$_POST['status'];


//Initialize

if(isset($method) && isset($status) && $method!="init" && $method!="electstatus" && $method!="writetotxt" && $method!="readfromtext"){
	toggleStatus($method,$status);
}

function toggleStatus($method,$status){
	system("gpio -g mode ".$method." out");
	system("gpio -g write ".$method." ".$status);
	system("gpio -g read ".$method);
}

if(isset($method) && $method=="init"){
	init();
}else if(isset($method) && $method=="electstatus"){
	electstatus();
}else if(isset($method) && $method=="writetotxt"){
	$file = $_POST['file'];
	$status = $_POST['status'];
	writetotxt($file,$status);
}else if(isset($method) && $method=="readfromtext"){
	$content = (string)$_POST['content'];
	readfromtext($content);
}

function init(){
	$pins = array(5,6,13);
	$count = count($pins);
	for($i=0;$i<$count; $i++){
		system("gpio -g read ".$pins[$i]);
	}
}


function electstatus(){
	$pins = array(12,16);
	$count = count($pins);
	for($i=0;$i<$count; $i++){
		system("gpio -g read ".$pins[$i]);
	}
}


function readfromtext($textids){

	$test = explode(",",$textids);
	$values=[];

	foreach ($test as $k => $v) {
    	$name = 'st'.$v.'.txt';
    	$value =  file_get_contents("txtFiles/".$name);
    	$test = str_replace(array("\r", "\n"),'', $value);	
    	array_push($values,$test);
	}
	echo json_encode($values);
}


function writetotxt($file,$status){


	if($status==0){
		
		$status=1;
		// if off, turn to on
	}else{
		// if on, turn to off
		$status=0;
	}
	
	$fullpath = $_SERVER['DOCUMENT_ROOT']."/Raspberry/txtFiles/st".$file.".txt";
	$f = fopen($fullpath, "w") or die("Unable to open File!");
	fwrite($f, $status); 
	fclose($f);
	if(file_get_contents($fullpath)==$status){
		echo 1;
	}else{
		echo 0;
	}
}

?>