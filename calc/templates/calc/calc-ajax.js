function ajaxBB(event){
		var form_type = BB_form;
		var sdano = document.getElementById("sdanoBB").value;
		var ordered_m = document.getElementById("ordered_mBB").value;
		var g_price = document.getElementById("g_priceBB").value;
		var min_m = document.getElementById("min_mBB").value;
		var radio = document.getElementsByName("BB").value;
		


		
		$.ajax({
			type: "POST",
			url: 'test-ajax',
			data: ({BB_form : BB_form, sdano : sdano, ordered_m : ordered_m, g_price : g_price, min_m : min_m, radio : radio}),
			dataType: 'text',
			success: function(data){  
            $('#result').text(data)
        	}  
         
		})
	}
