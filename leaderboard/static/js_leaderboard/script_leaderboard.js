$(document).ready(function(e){
    $.ajax({
        type: 'GET',
        url: window.location.href + "json",
        success: function(response) {

            $("#container").empty();

            $.get("/leaderboard/get-quote/", function(data) { // Get data from models via func in views
                addQuote($('#quote'), data);
            });
            
            for (let i = 0; i < response.length; i++) {
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

    if (searchUsername) {
        console.log("hi");
        $.get("/leaderboard/search/" + searchUsername + "/", function(data) { // Get data from models via func in views
            for (i = 0; i < data.length; i++) {
                // $.get("/leaderboard/getuser/" + (i+1) + "/", function(data_user) {
                //     addUserToLeaderboard($('#container'), data["fields"], data_user["fields"], data[i]["pk"]);
                // });
                addUserToLeaderboard($('#container'), data[i]["fields"], data[i]["pk"]);
            }
            if ($('#container').children().length == 0) {
                let html = `
                <div class="flex flex-col w-full rounded-md border border-gray-500 p-2 bg-gray-100">
                    <p class="text-lg justify-center italic font-semibold">Your search did not match any users :(</p>
                </div>`;

                $('#container').append(html);
            }
        });
    } else {
        let html = `
        <div class="flex flex-col w-full rounded-md border border-gray-500 p-2 bg-gray-100">
            <p class="text-lg justify-center italic font-semibold">Your search query is empty ^^</p>
        </div>`;

        $('#container').append(html);
    }
});


function addUserToLeaderboard($element, fields, user_id) { // Fields based on UserAccount    
    const name = fields["username"];

    const points = fields["user_point"];
    
    var html = 
    `
    <div class="col-md-12 infinite-item" id="user-${user_id}">
        <div class="shadow-md rounded-3xl mb-3 w-full bg-gradient-to-r from-cyan-500 to-white-0">
            <div class= "card-body flex justify-between px-5">
                <div>
                    <h2 class="font-semibold text-lg">${name}</h2>
                </div>
                <div>
                    <div class="text-sm"><span class="text-lg text-blue-600 italic">${points}</span> points</div>
                </div>
            </div>
        </div>
    </div>
    `
  
    $($element).append(html);
  }

$('#quote-user-btn').click(function(e) {
    e.preventDefault();

    let quoteMsg = $('#quotebox').val();

    $('#quotebox').val(""); // emptying the searchbox

    $('#quote').empty(); // emptying quote container
    $.get("/leaderboard/get-quote/", function(data) { // Get data from models via func in views
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
    var html = `
    <div class="flex flex-col w-full rounded-md border border-gray-500 p-2 bg-gray-100">
        <p class="text-lg justify-center italic font-semibold">"${quote}"</p>
        <div class="text-sm font-medium flex justify-end text-gray-600">~ by: ${name} ~</div>
    </div>
    `;

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
