plexRequests.controller('EditController', ['$rootScope', '$scope', '$http', 'requestService', 'commentService',
    function EditController($rootScope, $scope, $http, requestService, commentService) {

  $scope.markComplete = function(request) {
    $scope.loading = true;
    requestService.delete_request(request, function() {
      $scope.loading = false;
      $scope.refresh_requests();
    });
  };

  $scope.refresh_requests = function() {
    $scope.loading = true;
    requestService.get_all(function(requests) {
      $scope.requests = requests;
      $scope.loading = false;
    });
  };

  $scope.addComment = function(request, comment) {
    if (!comment) {
      return;
    }

    $scope.loading = true;
    commentService.addComment(request, comment, function() {
      $scope.loading = false;
      $scope.refresh_requests();
    });
  };

  $scope.deleteComment = function(request, comment) {
    $scope.loading = true;
    commentService.deleteComment(request, comment, function() {
      $scope.loading = false;
      $scope.refresh_requests();
    });
  };

  $scope.show = function(request) {
    $rootScope.$emit('show_item', request);
  };

  $rootScope.$on('refresh_needed', function(){
    $scope.refresh_requests()
  });

  $scope.refresh_requests();

}]);
