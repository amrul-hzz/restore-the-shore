$(document).ready(function(){

    $.get("/create-event/json/", function(data){
        for (i = 0; i < data.length; i++){
            getCard(data[i]);
            deleteCard(data[i]);
        }
    });

    function getCard(data){
        $("#history").append(
            `
            <div id="${data.pk}-card" class="max-w-sm rounded-lg overflow-hidden shadow-lg">
                <img class="w-full" src="${data.fields.fotoPantai}" alt="Gambar tidak ditemukan">
                <div class="px-6 pt-4">
                    <div class="font-bold text-xl mb-2">${data.fields.namaEvent}</div>
                    <div class="flex flex-row items-center gap-2 pt-2">
                        <div class="w-6 h-6">
                        <img src="https://cdn0.iconfinder.com/data/icons/gardening-glyph/2048/1939_-_Coconut_trees-512.png" alt="">
                        </div>
                        <div class="flex">${data.fields.namaPantai}</div>
                    </div>
                    <div class="flex flex-row items-center gap-3 pt-2">
                        <div class="w-5 h-5">
                        <img src="https://klinikmakmurjaya.com/assets/images/icon/99541b879c.png" alt="">
                        </div>
                        <div class="flex">${data.fields.alamatPantai}</div>
                    </div>
                    <div class="flex flex-row items-center gap-3 pt-2">
                        <div class="w-5 h-5">
                        <img src="https://icons.veryicon.com/png/o/internet--web/alibaba-cloud-classic-console-icon/time-and-date.png" alt="">
                        </div>
                        <div class="flex">${data.fields.tanggalMulai} - ${data.fields.tanggalAkhir}</div>
                    </div>
                </div>
                <div class="flex flex-row justify-center gap-2 pb-3">
                    <a class="cursor-pointer px-5 py-1 font-semibold bg-indigo-500 text-white mt-4 rounded-lg hover:bg-indigo-700 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none" href="/create-event/show-info/${data.pk}">More Info</a>
                    <a id="${data.pk}-delete" class="cursor-pointer px-5 py-1 font-semibold border-2 mt-4 rounded-lg hover:bg-green-500 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none">Delete</a>
                </div>
            </div>
            `
        );
    }

    function deleteCard(data) {
        $(`#${data.pk}-delete`).click(function () {
            $.post(`/create-event/delete-event/${data.pk}/`, {}).done(
            (card) => {
                $(`#${data.pk}-card`).fadeOut('slow');
            }
            );
        });
    }

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
            alert("The event has been successfully created");
            getCard(data);
            deleteCard(data);
            $("#namaEvent").val(""), 
            $("#namaPantai").val(""), 
            $("#alamatPantai").val(""), 
            $("#jumlahPartisipan").val(""), 
            $("#fotoPantai").val(""), 
            $("#output").attr('src', ''),
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