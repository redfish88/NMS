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


	 
