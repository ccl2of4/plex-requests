function EditController($rootScope, $scope, $http) {

  $scope.markComplete = function(request) {
    $scope.loading = true;
    $http({
      url : 'http://otis.ddns.net:5000/requests',
      method : 'DELETE',
      data : {'item' : request},
      headers: {'Content-Type': 'application/json' }
    }).then(function(response){
      $scope.loading = false;
      $scope.refresh_requests()
    });
  };

  $scope.refresh_requests = function() {
    $scope.loading = true;
    $http({
      url : 'http://otis.ddns.net:5000/requests',
      method : 'GET',
    }).then(function(data) {
      $scope.requests = data.data;
      $scope.loading = false;
    });
  };

  $scope.refresh_requests();
 
  $rootScope.$on('refresh_needed', function(){
    $scope.refresh_requests()
  });

  $scope.show = function(request) {
    $rootScope.$emit('show_item', request);
  };

}
