$(document).ready(function(){
    // $("#tambah").click(function(e){
    //     if ($("#namaEvent").val() == '' || $("#namaPantai").val() == '' || $("#alamatPantai").val() == '' || $("#jumlahPartisipan").val() == '' 
    //     || $("#fotoPantai").val() == '' || $("#deskripsi").val() == '' || $("#tanggalMulai").val() == '' || $("#tanggalAkhir").val() == '') {
    //         alert("input masih kosong");
    //     }
    // });

    $("#new-task").submit(function(e){
        e.preventDefault();
        $.post("/create-event/add/", { 
            namaEvent: $("#namaEvent").val(), 
            namaPantai: $("#namaPantai").val(),
            alamatPantai: $("#alamatPantai").val(), 
            jumlahPartisipan: $("#jumlahPartisipan").val(),
            fotoPantai: $("#fotoPantai").val(), 
            deskripsi: $("#deskripsi").val(),
            tanggalMulai: $("#tanggalMulai").val(),
            tanggalAkhir: $("#tanggalAkhir").val(),
        }).done(function (data) {
            $("#namaEvent").val(""), 
            $("#namaPantai").val(""), 
            $("#alamatPantai").val(""), 
            $("#jumlahPartisipan").val(""), 
            $("#fotoPantai").val(""), 
            $("#deskripsi").val(""), 
            $("#tanggalMulai").val(""), 
            $("#tanggalAkhir").val("");
        });
    });
});

var loadFile = function(event) {
    var output = document.getElementById('output');
    var link = document.getElementById('fotoPantai').value;
    output.src = link;
    output.classList.add("mt-1");
    output.classList.add("rounded-md");
    output.classList.add("p-2");
    output.classList.add("border");
    output.classList.add("border-slate-400");
};