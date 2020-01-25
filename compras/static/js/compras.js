$(document).ready(function() {
    $(".price").keyup(function() {
        var grandTotal = 0;
        $("input[name='qty[]']").each(function (index) {
            var qty = $("input[name='qty[]']").eq(index).val();
            var price = $("input[name='price[]']").eq(index).val();
            var output = parseInt(qty) * parseInt(price);

            if (!isNaN(output)) {
				$("input[name='output[]']").eq(index).val(output);
				grandTotal = parseInt(grandTotal) + parseInt(output);
            	$('#gran').val(grandTotal);
            }
        });
    });
});
