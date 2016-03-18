plexRequests.factory('commentService', ['$http',
    function CommentService($http) {

  function addComment(request, comment, completion) {
    $http({
      url : '/requests/' + request['request_id'] + '/comments',
      method : 'POST',
      data : {comment : {
        'content' : comment
      }}
    }).then(function(response){
      completion();
    });
  };

  function deleteComment(request, comment, completion) {
    $http({
      url : '/requests/' + request['request_id'] + '/comments/' + comment['comment_id'],
      method : 'DELETE',
    }).then(function(response){
      completion();
    });
  };

  return {
    addComment : addComment,
    deleteComment : deleteComment
  };

}]);
