plexRequests.controller('EditController', ['$rootScope', '$scope', '$http', 'requestService',
    function EditController($rootScope, $scope, $http, requestService) {

  $scope.markComplete = function(request) {
    $scope.loading = true;
    requestService.delete_request(request, function() {
      $scope.loading = false;
      $scope.refresh_requests()
    });
  };

  $scope.refresh_requests = function() {
    $scope.loading = true;
    requestService.get_all(function(requests) {
      $scope.requests = requests;
      $scope.loading = false;
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
