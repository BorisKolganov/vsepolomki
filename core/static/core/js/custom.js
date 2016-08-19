$(document).ready(function() {
	
	$("body").css("display", "none");

    $("body").fadeIn(600);
    
	$("a.transition").click(function(event){
		event.preventDefault();
		linkLocation = this.href;
		$("body").fadeOut(600, redirectPage);		
	});
		
	function redirectPage() {
		window.location = linkLocation;
	}
	
});
