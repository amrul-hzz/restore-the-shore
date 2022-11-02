
$(document).ready(function(){
    $.get(window.location.href + "json/", function (data) {
        for(i = 0; i < data.length; i++){
            appendPost(data[i]);   
        }
    });

    function appendPost(data){
        $("#forum-posts").append(
            `
                <div class="row" style="margin:5px;">
                    <div class="card" id="post-${data.pk}" style="outline:black;">
                       
                        <div class="card-body">
                            <p>${data.fields.creator_name}</p>
                            <hr>
                            <img src="${data.fields.image}" class="post-image"/>
                            <p class="card-content"> <b>${data.fields.creator_name}</b> ${data.fields.content}</p>
                            <p> Posted on ${data.fields.date} </p>
                            <a id="toggle-link-${data.pk}" data-toggle="collapse" href="#comments-${data.pk}" role="button" aria-expanded="false" aria-controls="comments-${data.pk}">
                                Show replies
                            </a>
                        </div>

                        <div class="card-footer text-muted"> 
                            <div class="collapse" id="comments-${data.pk}">
                                <form id="new-comment-form-${data.pk}" method="POST">

                                    <div id="comment-content-group" class="form-group">
                                        <input 
                                            type="text" 
                                            class="form-control" 
                                            id="comment-content-${data.pk}"
                                            name="comment-content" 
                                            placeholder="Write your comment here"
                                        />
                                    </div>

                                    <input type="submit" class="btn btn-primary" value="Submit" />
                                </form>  
                            </div>

                        </div>
                    </div>
                    
                    <script>
                        $("#new-comment-form-${data.pk}").submit(function(e){
                            e.preventDefault();

                            $.post("/forum/add-comment/" + ${data.pk} + "/", {
                                csrfmiddlewaretoken: '{{ csrf_token }}',
                                content: $("#comment-content-${data.pk}").val()
                            });

                           document.location.reload(true);
                            
                        });
                    <\/script>
                </div>
            `
        );

        appendAllComments(data);
        
    } 

    function appendComment(comment){
        $(`#no-comment-${comment.fields.original_post_id}`).empty();

        $(`#comments-${comment.fields.original_post_id}`).prepend(
            `
                <div id="comment-${comment.pk}-on-post-${comment.fields.original_post_id}">
                    <p> <b>${comment.fields.creator_name}</b> ${comment.fields.content} </p>
                </div>
            `
        );
    }

    function appendAllComments(currentPost){
        $.get(window.location.href + "json-comments/" + currentPost.pk + "/", function(comments){
            if (comments.length == 0) {
                $(`#comments-${currentPost.pk}`).prepend(
                    `<p id="no-comment-${currentPost.pk}">No comments yet</p>`
                );
            }
            else{
                for (i = 0; i < comments.length; i++) {
                    appendComment(comments[i]);
                }
                
            }
        });
    }

    $("#new-post-form").submit(function(e){
        e.preventDefault();

        $.post("/forum/add-post/", {
            content: $("#content").val(),
            image: $("#image").val()
        }).done(function(data){
            appendPost(data);

            const posts = document.getElementById("forum-posts");
            posts.insertAdjacentHTML("beforestart", `#post-${data.pk}`);
        });

        $("#staticBackdrop").modal("hide");
    });

});

