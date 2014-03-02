
$(document).ready(function() {
	loadFromJson("static/js/data.json");

	$('#header')
	.css({ 'top':-30 })
	.delay(1000)
	.animate({'top': 0}, 800);
	
	$('#footer')
	.css({ 'bottom':-15 })
	.delay(1000)
	.animate({'bottom': 0}, 800);
	
	
	$('#container').BlocksIt({
		numOfCol: 3,
		offsetX: 8,
		offsetY: 8
	});
	var currentWidth = 1100;
	$(window).resize(function() {
		var winWidth = $(window).width();
		var conWidth;
		if(winWidth < 660) {
			conWidth = 440;
			col = 2
		} else if(winWidth < 880) {
			conWidth = 660;
			col = 3
		} else if(winWidth < 1100) {
			conWidth = 880;
			col = 4;
		} else {
			conWidth = 1100;
			col = 5;
		}
		
		if(conWidth != currentWidth) {
			currentWidth = conWidth;
			$('#container').width(conWidth);
			$('#container').BlocksIt({
				numOfCol: col,
				offsetX: 8,
				offsetY: 8
			});
		}
	});
});

	


function addNewCard(html,size){
    var upperStyle = document.createElement("div");
	var card=document.createElement("div"); 
	
	$(card).attr({
    	"class" : "imgholder",
  	});
  	$(upperStyle).attr({
    	"class" : "grid",
  	});
  	$(card).html(html);
    $(upperStyle).html(card);
	$('#container').append(upperStyle);
}

function loadFromJson(JsonUrl){
	$.ajax({
  		url: JsonUrl,
  		dataType: 'json',
  		async:false,
  		success: function(data){
  	      $.each(data, function(i, item) {
			titleHtml="<h3>"+item.title+"</h3>";
			img="<img src=" + item.imgSrc+ "></img>";
			content ="<h3>"+item.content+"</h3>";
			html=img+titleHtml+content;
    	    addNewCard(html,item.size);     
        })
	}
});
	
}
