function setUrl()
{
	var techtype="Sencha";
	var widgetType="panel";
	var roleval=$(event.srcElement).data("role");
	if(roleval=="source")
	{
		var resolver=$(event.srcElement).data("role")+".js";
	
		$("#contentdoc")[0].innerHTML="<iframe src='Documents/"+techtype+"/"+widgetType+"/"+resolver+"'></iframe>";
		console.log(window.document.URL+"/"+resolver);
	}
	else
	{
	var resolver=$(event.srcElement).data("role")+".html";
	}
	
	var path="Documents/"+techtype+"/"+widgetType+"/"+resolver;
	if($(event.srcElement).data("role")=="source")
	{ 
		$("#headingattr")[0].innerHTML="source-code ("+widgetType+")";
		$("#docjumbo").removeClass().addClass("jumbotron  active btn-success");;
		//$("#docjumbo").addClass("jumbotron  active btn-success");


	 }
	else if($(event.srcElement).data("role")=="settings")
	{ 
		$("#headingattr")[0].innerHTML="Settings ("+widgetType+")";
		$("#docjumbo").removeClass().addClass("jumbotron active btn-info");
		//$("#docjumbo").
	}
	else if($(event.srcElement).data("role")=="Document")
	{ 
		$("#headingattr")[0].innerHTML="Document ("+widgetType+")";
		$("#docjumbo").removeClass().addClass("jumbotron active btn-primary");
		//$("#docjumbo").addClass("jumbotron active btn-primary");
	}
	else if($(event.srcElement).data("role")=="specs")
	{ 
		$("#headingattr")[0].innerHTML="Specification ("+widgetType+")";
		$("#docjumbo").removeClass().addClass("jumbotron active btn-warning");
	
	}
	
	console.log(path);
	$.ajax({
		url:path,
		success:function(result){
				
				$("#contentdoc")[0].innerHTML=result;
		}
	});
}