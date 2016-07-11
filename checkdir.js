var fs=require("fs");
var appName="TutorialApp";

var appPath='C:\\Users\\Himanshu\\bin\\Sencha\\Cmd\\TutorialApp';
//making module files for classic 
var viewPath=appPath+"\\classic\\src\\view\\";

//modulePath init
var modPath=viewPath+"\\check3";

console.log(viewPath);
//making folders in classic view folder
fs.mkdir(modPath,function(err){
	if(err)
	{
		console.log(err);
		console.log("You might not have write access or dir already exisist");
	}

});

//read the baseTemplate files and create Files for modules
fs.readFile("sourcetemplates/storetemplate.js",function(err,data){
	if(err){return console.log(err);}
	var parsedstore=data.toString();
	fs.writeFile(modPath+"\\check3"+"store.js",parsedstore);
	console.log(parsedstore);
}
);

//reading  the controllertemplate
fs.readFile("sourcetemplates/controllertemplate.js",function(err,data){
	if(err){return console.log(err);}
	var parsedcontroller=data.toString();
    fs.writeFile(modPath+"\\check3"+"controller.js",parsedcontroller);
	console.log(parsedcontroller);
}
);


//reading  the viewtemplate
fs.readFile("sourcetemplates/viewtemplate.js",function(err,data){
	if(err){return console.log(err);}

	var parsedView=data.toString();
	var refname=appName+".view."+"check3.check3"+"view";
	var dataTowrite=parsedView.replace("placeholder1",refname).replace("placeholder2","check3").replace("placeholder3","check3");;
	fs.writeFile(modPath+"\\check3"+"view.js",dataTowrite);
	console.log(parsedView);
});


//reading  the viewtemplate
fs.readFile("sourcetemplates/viewmodeltemplate.js",function(err,data){
	if(err){return console.log(err);}

	var parsedView=data.toString();
	var refname=appName+".view."+"check3.check3"+"viewModel";
	console.log(refname);
	var dataTowrite=parsedView.replace("placeholder1",refname).replace("placeholder2","viewmodel.checkviewmodel");
	fs.writeFile(modPath+"\\check3"+"viewModel.js",dataTowrite);
	console.log(parsedView);
}
);
