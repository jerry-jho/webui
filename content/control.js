$(document).ready(function() {
    new QWebChannel(qt.webChannelTransport, function(channel) {
        var my_object = channel.objects.MyObject;
        $("#btn0").click(function() {
            my_object.consolePrint($("#txt0").val());
        });
        $("#btn1").click(function() {
            my_object.setParentWindowTitle($("#txt1").val());
        });   
        $("#btn2").click(function() {
            my_object.saveFile($("#txt2").val(),$("#txt3").val());
        });        
        var my_timer = channel.objects.MyTimer;
        my_timer.timeout.connect(function() {
            $("#ctr0").text(1 + parseInt($("#ctr0").text()));
        });
        my_timer.start(2000);
    })
})
