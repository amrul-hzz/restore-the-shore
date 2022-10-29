$(document).ready(function(e){
    $.ajax({
        type: 'GET',
        url: window.location.href + "json",
        success: function(response) {
            for (let i = 0; i < response.length; i++) {
                addUserToLeaderboard($('.infinite-container'), response[i]["fields"], response[i]["pk"]);
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


    $.post("/leaderboard/search/" + searchUsername + "/", {}).done( (e) => {
        $.get("/leaderboard/search/" + searchUsername + "/", function(data) { // Get data from models via func in views
            for (i = 0; i < data.length; i++) {
                addUserToLeaderboard($('#container'), data[i]["fields"], data[i]["pk"]);
            }
        });
    });
});

function addUserToLeaderboard($element, fields, user_id) { // Fields based on UserAccount
    const user = fields["user"];
    const name = user["username"];
    const points = fields["user_point"];
  
    var html = 
    `<div class="col-md-12 infinite-item" id="user-${user_id}">
        <div class="card mb-4 box-shadow">
            <div class= "card-body">
                <h2 style="font-size:18px;font-weight:bold;min-height:42px;">
                    ${name}</h2>
                <!-- <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">${points} points</small>
                </div> -->
            </div>
        </div>
    </div>`
  
    $($element).append(html);
  }


$('#quote-user-btn').click(function(e) {
    e.preventDefault();

    let quoteMsg = $('#quotebox').val();

    $('#quotebox').val(""); // emptying the searchbox

    $('#container').empty(); // emptying container

    if (quoteMsg) {
        $.post("/leaderboard/add-quote/" + quoteMsg + "/", {}).done( (e) => {
            $.get("/leaderboard/add-quote/" + quoteMsg + "/", function(data) { // Get data from models via func in views
                addQuote($('#quote', data));
            });
        });
    }
})

function addQuote($element, data) {
    const quote = data["random-quote"];
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
