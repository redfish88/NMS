   $(function() {

   		$("#sign").click(function(){

   			var username = $("#username").val();
   			var password = $("#password").val();
   			if( username == null || username == ''){
   				$("#errmsg").html("用户名不能为空");
   				return;

   			}
   			if( password == null || password == ''){
   				$("#errmsg").html("密码不能为空");
   				return;

   			}else{
   				$("#form1").submit();
   			}
   		

   		}


   		)

   	})