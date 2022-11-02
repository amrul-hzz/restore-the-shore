$(document).ready(function(){
    loadData();
   
    
  })

  

  const card = (data) => `
    
      <div class ="card ratio-4x3" id="${data.pk}-card">
          <div class="card-header overflow-hidden p-0">
  
          <img class="w-40 h-30 card-img-top" src=${data.fields.fotoPantai} id="${data.pk}-foto">

        
          </div>
          
          <div class="card-body">
          


          <h5 class="card-title" id= "${data.pk}-namaPantai">Pantai: ${data.fields.namaPantai}</h5>
          <h5 class="card-title" id= "${data.pk}-alamatPantai">Lokasi: ${data.fields.alamatPantai}</h5>
          <h5 class="card-title" id= "${data.pk}-tanggalMulai">Tanggal Mulai: ${data.fields.tanggalMulai}</h5>
          <h5 class="card-title" id= "${data.pk}-tanggalAkhir">Tanggal Akhir: ${data.fields.tanggalAkhir}</h5>

          
          
          
          </div>

          <div class="card-footer justify-content-center">
            <a href="event_detail/${data.pk}", class="btn btn-primary">Read More</a>
          </div>
      </div>
      <br>
      `

  function loadData(){
    $.get('../create-event/json/', function (data) {
      for(var i = 0; i < data.length; i++){
     
        $('#data_list').append(card(data[i]))
      }
  })
  }