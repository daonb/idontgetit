document.addEventListener('mouseup',function(event)
{
	var sel = window.getSelection().toString();
	var url = top.location.href;
	
	if(sel.length)
		chrome.extension.sendRequest({'message':'setText','data': sel },function(response){})
})

