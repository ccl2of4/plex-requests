plexRequests.factory('commentService', ['$http', 'apiService',
    function CommentService($http, api) {

      return {
        addComment : addComment,
        deleteComment : deleteComment
      };

      function addComment(request, comment, completion) {
        $http({
          url : api.buildUrl('/requests/', request['request_id'], '/comments'),
          method : 'POST',
          data : {
            'content' : comment
          }
        }).then(function(response){
          completion();
        });
      };

      function deleteComment(request, comment, completion) {
        $http({
          url : api.buildUrl('/requests/', request['request_id'], '/comments/', comment['comment_id']),
          method : 'DELETE',
        }).then(function(response){
          completion();
        });
      };

}]);
