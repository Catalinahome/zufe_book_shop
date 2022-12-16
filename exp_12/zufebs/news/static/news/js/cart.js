$(function(){
    $.calc = function(){
        check = $(".select>input");
        price = $(".cprice>span");
        num = $(".cnum>input[type='text']");
        total = $(".ctotal>span");
        var sum = 0;
        var cnt = 0;
        for(i=0; i<price.size(); i++){
            var subtotal = Math.round(price.eq(i).html()*num.eq(i).val()*100)/100;
            total.eq(i).html(subtotal);
            if(check.eq(i).attr("checked")){
                sum += subtotal;
                cnt += parseInt(num.eq(i).val());
            }
        }
        $("#sum_num").html(cnt);
        $("#sum_price").html(sum);
    }

    $.calc();
    
    $(".cartitem>.cnum>input[type='text']").blur(function(){
        $.calc();
    })

    $(".cartitem>.cnum>input[value='-']").click(function(){
        var val = parseInt($(this).parent().find("input[type='text']").val());
        if(val>0){
            $(this).parent().find("input[type='text']").val(val-1);
            $.calc();
        }else{
            $(this).parent().find("input[type='text']").val(0)
        }
    })

    $(".cartitem>.cnum>input[value='+']").click(function(){
        $(this).parent().find("input[type='text']").val(parseInt($(this).parent().find("input[type='text']").val())+1)
        $.calc();
    })

    $(".select>input").click(function(){
        $.calc();
    })

    $(".select0>input").click(function(){
        $(".select>input").attr("checked", $(this).attr("checked"));
        $.calc();
    })

})