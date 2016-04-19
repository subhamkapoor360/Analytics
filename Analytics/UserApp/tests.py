from django.test import TestCase

# Create your tests here.
'''
    <!-- Custom Theme JavaScript     <script src="js/agency.js"></script>
     <script type = "text/javascript" 
         src = "https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
      <script type = "text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>

      <script type = "text/javascript">
      $(document).ready(function() {
          
       $("#submit").on('click',function(event){
        console.log("button");
        submitChanges();
       });

       function submitChanges(){
          var newData = {

                           'name': $('#name').val(),
                           'userId': $('#username').val(),
                           'password': $('#password').val(),
                           'gender': $('#gender').val(),
                           'mobileNo': $('#mobileno').val(),
                           'emailId': $('#email').val(),
                     
          };
            $.ajax({
                     type:"POST",
                     url:"/registeruser/",
                     contentType: "application/x-www-form-urlencoded",
                     dataType:'json',
                     data : newData,
                     success: function(response,textstatus, jqXHR){
                        console.log("textstatus");
                        if(response.resCode == "0"){
                        var responseData = response.resDet.register;
                        //window.location.href()
                        console.log(responseData);
                      }else{
                        console.log("a");


                      }
                        //alert( "User Saved:");
                 },
                 error: function(response,textstatus,jqXHR){
                  console.log(response);
                 }
            });
          }
        
          //return false; // move it here
       });



      </script> 
-->'''