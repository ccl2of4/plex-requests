plexRequests.factory('commentService', ['$http', 'envService',
    function CommentService($http, envService) {

  function addComment(request, comment, completion) {
    $http({
      url : getUrl('/requests/' + request['request_id'] + '/comments'),
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
      url : getUrl('/requests/' + request['request_id'] + '/comments/' + comment['comment_id']),
      method : 'DELETE',
    }).then(function(response){
      completion();
    });
  };

  function getUrl(endpoint) {
    return envService.read('apiBaseUrl') + endpoint;
  };

  return {
    addComment : addComment,
    deleteComment : deleteComment
  };

}]);
