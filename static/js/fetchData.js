// fetchData.js
function fetchData() {
    $.ajax({
        url: '/readPLC',
        type: 'GET',
        success: function(data) {
            $('#plcValue').text(data.data_int);
            $('#plcValue1').text(data.data_int_1);
            $('#plcValue2').text(data.data_int_2);
            $('#plcValue3').text(data.data_int_3);

        },
        error: function(error) {
            $('#plcValue').text('None');
            $('#plcValue1').text('None');
            $('#plcValue2').text('None');
            $('#plcValue3').text('None');


        }
    });
}

// Refrescar cada 1000 ms (1 segundo)
setInterval(fetchData, 1000);

