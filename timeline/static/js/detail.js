
$(document).ready(function(){  
    $(`.button`).click(function () {
        var info = $('.button').attr('id');
        var dataSimpan;
        let ada = null;
        $.get("/timeline/json/", function(data){
            for (i = 0; i < data.length; i++){
                if (data[i].fields.namaEvent == info){
                    ada = true;
                    break;
                }
                ada = false;
            }
            if (ada === true) {
                alert("Event sudah diikuti")
            } else {
                $.get("/create-event/json/", function(data){
                    for (i = 0; i < data.length; i++){
                        if (data[i].fields.namaEvent == info){
                            dataSimpan = data[i];
                            break;
                        }
                    }
                    $.post("/timeline/joinevent/",
                    {
                        namaEvent : dataSimpan.fields.namaEvent,
                        namaPantai: dataSimpan.fields.namaPantai,
                        alamatPantai: dataSimpan.fields.alamatPantai,
                        jumlahPartisipan: dataSimpan.fields.jumlahPartisipan,
                        fotoPantai: dataSimpan.fields.fotoPantai,
                        deskripsi: dataSimpan.fields.deskripsi,
                        tanggalMulai: dataSimpan.fields.tanggalMulai,
                        tanggalAkhir: dataSimpan.fields.tanggalAkhir,
                    },
                    function (data,status){
                        alert("Event berhasil diikuti");
                    }
                )
                })
            }
        })
        })
})