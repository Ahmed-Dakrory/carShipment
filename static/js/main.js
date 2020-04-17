window.setInterval(function(){
    $.ajax({
                url: '/ajax_conPro' ,
                data: {
                'inputValue': "data_to_context"
                },
                dataType: 'json',
                success: function (data) {
                document.getElementById('ptime').innerHTML = data["current_date"];
                }
            });
        
}, 500);