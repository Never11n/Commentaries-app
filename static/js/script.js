const socket = new WebSocket('ws://' + window.location.host + '/ws/');

    socket.onmessage = function (e) {
        let data = JSON.parse(e.data);
        let commentsContainer = document.getElementById('comments-container');
        let p = document.createElement('p');
        p.textContent = data.comment.name + ' написал(а) ' + data.comment.comment_text + '.';
        commentsContainer.appendChild(p);
    }
    function selectedCommentId(parent_id){
        let parentIdInput = document.getElementById("id_parent_comment_id")
        parentIdInput.value = parent_id
    }