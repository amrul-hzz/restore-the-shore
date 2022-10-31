$(document).ready(function(e){
    $.ajax({
        type: 'GET',
        url: window.location.href + "json",
        success: function(response) {

            console.log(response)
            $("#container").empty();
            
            for (let i = 0; i < response.length; i++) {
                // $.get("/leaderboard/getuser/" + (i+1) + "/", function(data_user) {
                //     console.log(data_user)
                //     addUserToLeaderboard($('#container'), response["fields"], data_user["fields"], response[i]["pk"]);
                // });
                addUserToLeaderboard($('#container'), response[i]["fields"], response[i]["pk"]);
            }
        },
        error: function(response) {
            console.log(response);
        }
    })
});

$("#search-user-btn").click(function(e) {
    e.preventDefault();

    let searchUsername = $('#searchbox').val();

    $('#searchbox').val(""); // emptying the searchbox

    $('#container').empty(); // emptying container


    
    $.get("/leaderboard/search/" + searchUsername + "/", function(data) { // Get data from models via func in views
        for (i = 0; i < data.length; i++) {
            // $.get("/leaderboard/getuser/" + (i+1) + "/", function(data_user) {
            //     addUserToLeaderboard($('#container'), data["fields"], data_user["fields"], data[i]["pk"]);
            // });
            addUserToLeaderboard($('#container'), data[i]["fields"], data[i]["pk"]);
        }
    });
   
});

// function addUserToLeaderboard($element, useraccount_fields, user_fields, user_id) { // Fields based on UserAccount
//     const name = user_fields["username"];

//     console.log(user_fields["user"]);

//     const points = useraccount_fields["user_point"];
  
//     var html = 
//     `<div class="col-md-12 infinite-item" id="user-${user_id}">
//         <div class="card mb-4 box-shadow">
//             <div class= "card-body">
//                 <h2 style="font-size:18px;font-weight:bold;min-height:42px;">
//                     ${name}</h2>
//                 <div class="d-flex justify-content-between align-items-center">
//                     <small class="text-muted">${points} points</small>
//                 </div>
//             </div>
//         </div>
//     </div>`
  
//     $($element).append(html);
//   }

function addUserToLeaderboard($element, fields, user_id) { // Fields based on UserAccount
    const name = fields["username"];

    const points = fields["user_point"];
  
    var html = 
    `<div class="col-md-12 infinite-item" id="user-${user_id}">
        <div class="card mb-4 box-shadow">
            <div class= "card-body">
                <h2 style="font-size:18px;font-weight:bold;min-height:42px;">
                    ${name}</h2>
                <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">${points} points</small>
                </div>
            </div>
        </div>
    </div>`
  
    $($element).append(html);
  }

$('#quote-user-btn').click(function(e) {
    e.preventDefault();

    let quoteMsg = $('#quotebox').val();

    $('#quotebox').val(""); // emptying the searchbox

    $('#quote').empty(); // emptying quote container
    $.get("/leaderboard/add-quote/", function(data) { // Get data from models via func in views
        addQuote($('#quote'), data);
    });
    if (quoteMsg) {
        $.post("/leaderboard/add-quote/", {
            "quote": quoteMsg
        });
    }
})

function addQuote($element, data) {
    const quote = data["random_quote"];
    const name = data["name"];
    var html = `<p class="lead">${quote} by ${name}</p>`;

    $($element).append(html);
}

var infinite = new Waypoint.Infinite({
    element: $('.infinite-container')[0],

    offset: 'bottom-in-view',

    onBeforePageLoad: function () {
        $('.spinner-border').show();
    },
    onAfterPageLoad: function () {
        $('.spinner-border').hide();
    }

});
