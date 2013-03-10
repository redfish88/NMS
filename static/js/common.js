if(!String.prototype.trim) {
  String.prototype.trim = function () {
    return this.replace(/^\s+|\s+$/g,'');
  };
}
function preview(){
	var  result = $("#md-editor").val();
	$('#preview').html(markdown.toHTML(result));
	$('#md-editor').hide();
	$('#preview').show();

}
function editor(){
	$('#md-editor').show();
	$('#preview').hide();

}
//存为草稿（撤销发布)
function to_draft(){
	validate_news();
	//设置状态为0 草稿
	$('#status').val(0);
	$("#form-news").submit();
}
//保存 不改变状态
function save(status){
	validate_news();
	$("#form-news").submit();

}
//发布
function to_post(){

	validate_news();
	$('#status').val(1);
	$("#form-news").submit();
}
function validate_news(){
	var title = $("#pb-text-title").val();
	var content = $("#md-editor").val();
	if(title == '' || title == null){
		alert("标题不能为空");
		return;
	}
	if(content == '' || content == null){
		alert("正文不能为空");
		return;
	}

}
function draft(){
	var title = $("#pb-text-title").val();
	var content = $("#md-editor").val();
	if(title == '' || title == null){
		alert("标题不能为空");
		return;
	}
	if(content == '' || content == null){
		alert("正文不能为空");
		return;
	}else{
		//设置状态为0 草稿
		$('#status').val(0);
		$("#form-news").submit();
	}


}
function publish(){

	var title = $("#pb-text-title").val();
	var content = $("#md-editor").val();
	if(title == '' || title == null){
		alert("标题不能为空");
		return;
	}
	if(content == '' || content == null){
		alert("正文不能为空");
		return;
	}else{
		//设置状态为1 发布
		$('#status').val(1);
		$("#form-news").submit();
	}
}
function votePost(post_id,type){
	var result = $.cookie('news_'+post_id);
	if(result){
		if(result == 'top')
		 {
		 	$('#digg_tips').html("您已经顶过!")
		 }
		 else{
		 	$('#digg_tips').html("您已经踩过!")
		 }
		return;

	}else{
		
		$.post( "/vote_post" , {
	    	post_id : post_id,
	    	type	: type
        },
        function(result) {
            if(result == 'success'){
            	old_value = $("#"+type).html();
            	new_value = parseInt(old_value)+1;
            	$("#"+type).html(new_value);
            	$.cookie('news_'+post_id,type,{expires:365,path:'/'});
            }


        });
	}



}
function pre_submit(){

	var username = $("#username").val()
	var password = $("#passwd").val()
	var confirmpw = $("#confirm-passwd").val()
	if (username == null || username.trim()==""){
		$("#errmsg").html("用户名不能为空");
		return;
	}
	if (password == null || password.trim()==""){
		$("#errmsg").html("密码不能为空");
		return;
	}
	if (confirmpw.trim() != password.trim() ){
		$("#errmsg").html("两次密码不一致");
		return;
	}else{
		$("#username").val(username.trim());
		$("#passwd").val(password.trim());
		$("#form-signup").submit();

	}

}


	 
