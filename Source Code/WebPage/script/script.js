jQuery(document).ready(function(){


jQuery('#action_section').on('click','.button',function(){

	var method = jQuery(this).attr('data-method');
	var status = jQuery(this).attr('data-status');
	var button = jQuery(this)[0];
	toggleStatus(method,status,button);

});


jQuery('#preset_section').on('click','.button',function(){

   var method = jQuery(this).attr('data-method');
   var status = jQuery(this).attr('data-status');
   var button = jQuery(this)[0];
   togglePreset(method,status,button);
});





function toggleStatus(method,status,button){

	jQuery.ajax({
      url: 'functions.php',
      data: {
         method: method,
         status: status
      },
      type: 'POST',
      error: function() {
         alert('Something is wrong.');
      },
      success: function(data) {
      	if(data==1){
      		jQuery(button).attr('data-status','0');
      		jQuery(button).text('Off');
            jQuery(button).addClass('off');
            jQuery(button).removeClass('on');
      	}else{
      		jQuery(button).attr('data-status','1');
      		jQuery(button).text('On');
            jQuery(button).removeClass('off');
            jQuery(button).addClass('on');
      	}
      }
   });
}



function togglePreset(method,status,button){

   jQuery.ajax({
      url: 'functions.php',
      data: {
         method: 'writetotxt',
         status: status,
         file: method
      },
      type: 'POST',
      error: function() {
         alert('Something is wrong.');
      },
      success: function(data) {

         if(data==1){


            if(status==0){

               jQuery(button).attr('data-status','1');
               jQuery(button).text('Turn On');
               jQuery(button).addClass('on');
            }else{
               jQuery(button).attr('data-status','0');
               jQuery(button).text('Keep Off');
               jQuery(button).removeClass('on');
            }


         }

         // if(data==1){
         //    jQuery(button).attr('data-status','0');
         //    jQuery(button).text('Turn On');
         //    jQuery(button).addClass('off');
         //    jQuery(button).removeClass('on');
         // }else{
         //    jQuery(button).attr('data-status','1');
         //    jQuery(button).text('Turn Off');
         //    jQuery(button).removeClass('off');
         //    jQuery(button).addClass('on');
         // }
      }
   });
}





function init(){
   var initArrays=[];
	jQuery.ajax({
      url: 'functions.php',
      data: {
         method: 'init',
      },
      type: 'POST',
      error: function() {
         alert('Something is wrong.');
      },
      success: function(data) {
             //loop in data to assign to each button its value returned from init function             
      initArrays = data.replace(/(\r\n|\n|\r)/gm,"").split("");
      
      $.each(initArrays,function(k,i){


         if(i==1){
            jQuery('#action_section .button').eq(k).attr('data-status','0');
            jQuery('#action_section .button').eq(k).text('Off')
            jQuery('#action_section .button').eq(k).addClass('off');
            jQuery('#action_section .button').eq(k).removeClass('on');
         }else{
            jQuery('#action_section .button').eq(k).attr('data-status','1');
            jQuery('#action_section .button').eq(k).text('On')
            jQuery('#action_section .button').eq(k).addClass('on');
            jQuery('#action_section .button').eq(k).removeClass('off');
         }
      });
      }
   });
}

function electstatus(){
   var initArrays=[];
   jQuery.ajax({
      url: 'functions.php',
      data: {
         method: 'electstatus',
      },
      type: 'POST',
      error: function() {
         alert('Something is wrong.');
      },
      success: function(data) {
         initArrays = data.replace(/(\r\n|\n|\r)/gm,"").split("");

         $.each(initArrays,function(k,i){
         if(i==1){   
            jQuery('#electstatus .item').eq(k).addClass('off');
         }else{
            jQuery('#electstatus .item').eq(k).addClass('on');
         }
      });
      }
   });
}


function readfromtxt(){

   var initMethods=[];

    $('#preset_section .button.preset').each(function(k,i){
      var method = $(this).attr('data-method'); 
      initMethods.push(method);
    });

      var stringify  = initMethods.toString();
     jQuery.ajax({
         url: 'functions.php',
         data: {
            method: 'readfromtext',
            content: stringify,
         },
         type: 'POST',
         error: function() {
            alert('Something is wrong.');
         },
         success: function(data) {
            var results = JSON.parse(data);
            for(i=0;i<results.length;i++){
               $('#preset_section .button.preset').eq(i).attr('data-status',results[i]);
               if(results[i]==1){
                  $('#preset_section .button.preset').eq(i).addClass('on').text('Turn On');
               }
           }

         }
      });
}

readfromtxt();




      // jQuery.ajax({
      //       url: 'functions.php',
      //       data: {
      //          method: 'readfromtext',
      //          content: "testing!!!!",
      //          file: "st13.txt"
      //       },
      //       type: 'POST',
      //       error: function() {
      //          alert('Something is wrong.');
      //       },
      //       success: function(data) {
      //          alert(data);
      //       }
      //    });


init();
electstatus();
});