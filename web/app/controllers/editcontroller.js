plexRequests.controller('EditController', ['$rootScope', '$scope', '$http', 'requestService', 'commentService',
    function EditController($rootScope, $scope, $http, requestService, commentService) {

  (function init() {
    refreshRequests();
    $rootScope.$on('refreshNeeded', function(){
      refreshRequests()
    });
  })();

  function refreshRequests() {
    $scope.loading = true;
    requestService.getAll(function(requests) {
      $scope.requests = requests;
      $scope.loading = false;
    });
  };

  function deleteRequest(request) {
    $scope.loading = true;
    requestService.deleteRequest(request, function() {
      $scope.loading = false;
      $scope.refreshRequests();
    });
  };

  function showCommentBox(request) {
    $scope.commentingRequest = request;
  };

  function showingCommentBox(request) {
    return $scope.commentingRequest == request;
  };

  function addComment(request, comment) {
    if (!comment) {
      return;
    }

    $scope.loading = true;
    commentService.addComment(request, comment, function() {
      $scope.loading = false;
      $scope.refreshRequests();
    });
  };

  function addCommentIfEnterKeyPressed($event, request, newComment) {
    if ($event.which === 13) {
      addComment(request, newComment);
    }
  };

  function deleteComment(request, comment) {
    $scope.loading = true;
    commentService.deleteComment(request, comment, function() {
      $scope.loading = false;
      $scope.refreshRequests();
    });
  }

  function show(request) {
    $rootScope.$emit('showItem', request);
  };

  $scope.refreshRequests = refreshRequests;
  $scope.deleteRequest = deleteRequest;
  $scope.showCommentBox = showCommentBox;
  $scope.showingCommentBox = showingCommentBox;
  $scope.addCommentIfEnterKeyPressed = addCommentIfEnterKeyPressed;
  $scope.addComment = addComment;
  $scope.deleteComment = deleteComment;
  $scope.show = show;

}]);
