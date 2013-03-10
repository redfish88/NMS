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


	 
