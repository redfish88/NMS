$(function() {



	$.getJSON('/vote_post',{
		post_id : $("#post_id").val()
	},function(result){
		if(result.length > 0){
			hot = result[0]
			$("#top").html(hot.top);
			$("#stamp").html(hot.stamp);
		}

	})
	//document.getElementById('content').innerHTML=markdown.toHTML(document.getElementById('content-hide').value);
	$('#content').html(markdown.toHTML($('#content-hide').val()));
	var post_id = $("#post_id").val();
	var result = $.cookie('news_font_'+post_id);
	if(result){
		$('#content').css({'font-size':result+'px'})
	}

})
function doZoom(size){
	var post_id = $("#post_id").val();
	$('#content').css({'font-size':size+'px'})
	$.cookie('news_font_'+post_id,size,{expires:365,path:'/'});
}