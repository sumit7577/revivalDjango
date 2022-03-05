$(document).ready(function(){
	"use strict";

    // 1. Scroll To Top 
		$(window).on('scroll',function () {
			if ($(this).scrollTop() > 600) {
				$('.return-to-top').fadeIn();
			} else {
				$('.return-to-top').fadeOut();
			}
		});
		$('.return-to-top').on('click',function(){
				$('html, body').animate({
				scrollTop: 0
			}, 1500);
			return false;
		});
	
	
	// 2. owl carousel
	
		// i. client (carousel)
		
			$('#client').owlCarousel({
				items:5,
				loop:true,
				smartSpeed: 1000,
				autoplay:true,
				dots:false,
				autoplayHoverPause:true,
				responsive:{
						0:{
							items:2
						},
						415:{
							items:3
						},
						600:{
							items:3

						},
						1200:{
							items:5
						}
					}
				});
				
				
				$('.play').on('click',function(){
					owl.trigger('play.owl.autoplay',[1000])
				})
				$('.stop').on('click',function(){
					owl.trigger('stop.owl.autoplay')
				})

		// ii.  testimonial-carousel
		
			$("#collection-carousel").owlCarousel({
				items: 1,
				autoplay: true,
				loop: true,
				dots:false,
				mouseDrag:true,
				nav:false,
				smartSpeed:1000,
				transitionStyle:"fade",
				animateIn: 'fadeIn',
				animateOut: 'fadeOutLeft'
				// navText:["<i class='fa fa-angle-left'></i>","<i class='fa fa-angle-right'></i>"]
			});


    // 3. welcome animation support

        $(window).load(function(){
        	$(".welcome-hero-txt h4,.welcome-hero-txt h2,.welcome-hero-txt p").removeClass("animated fadeInUp").css({'opacity':'0'});
            $(".welcome-hero-txt button").removeClass("animated fadeInDown").css({'opacity':'0'});
        });

        $(window).load(function(){
        	$(".welcome-hero-txt h4,.welcome-hero-txt h2,.welcome-hero-txt p").addClass("animated fadeInUp").css({'opacity':'0'});
            $(".welcome-hero-txt button").addClass("animated fadeInDown").css({'opacity':'0'});
        });


	// 4. cart-close
		$(".cart-close").click(function(){
			$(this).parents(".single-cart-list").fadeOut();
		});

});


let value = document.getElementById("scroll-button").attributes.class.value;
let mainNavbar = document.getElementById("navbarMain")
setInterval(() =>{
	if(value == "navbar-toggle"){
		mainNavbar.classList.add("sticked");
	}
	else{
		mainNavbar.classList.remove("sticked");
	}
},1000)


//Modal Logic


let imageButtons = document.getElementsByClassName("imageOverlay");
for(let i of imageButtons){
	i.addEventListener("click",function(e){
		let overlay = document.getElementsByClassName("lb-container");
		if(overlay[0].firstChild.nextSibling.nextSibling.nextSibling != undefined){
			overlay[0].removeChild(overlay[0].children[3]);
		}
		let textElement = document.createElement("div");
		textElement.classList.add("fightDetails");
		let header = document.createElement("h1");
		let desc = document.createElement("h2");
		let time = document.createElement("h2");
		let location = document.createElement("h2");
		desc.innerText = "Description:"+" "+this.attributes.desc.value;
		header.innerText = this.attributes.name.value;
		time.innerText = "Time:"+" "+this.attributes.time.value;
		location.innerText = "Location:"+" "+this.attributes.loc.value;
		textElement.appendChild(header);
		textElement.appendChild(desc);
		textElement.appendChild(time);
		textElement.appendChild(location);
		overlay[0].appendChild(textElement);
	})
}
