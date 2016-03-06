function RequestController($rootScope, $scope, $http, $q) {

  $scope.searchtype = 'movie';

  $scope.$watch('query', function(query) {
    refresh(query);
  });

  $scope.$watch('searchtype', function(searchType) {
    refresh($scope.query);
  });

  $rootScope.$on('show_item', function(event, request) {
    $scope.searchtype = request.type;
    $scope.query = request.name;
  });

  $scope.add = function(searchresult) {
    $scope.loading = true;
    $http({
      url : postUrl(),
      method : 'POST',
      data : postParams(searchresult),
    }).then(function(response){
      $scope.loading = false;
      $rootScope.$emit('refresh_needed');
    });
  };

  var refresh = function(query) {
    cancelRequest();
    if (!query) {
      $scope.searchresults = [];
      return;
    }

    search(query);
  },

  search = function(query) {
    $scope.loading = true;
    $http({
      url : getUrl(),
      method : 'GET',
      params : {query : query},
      timeout : $scope.canceller.promise
    }).then(completeRequest);
  },

  postParams = function(searchresult) {
    return $scope.searchtype == 'movie' ?
      { movie : searchresult } :
      { tv_show : searchresult };
  },

  postUrl = function() {
    return $scope.searchtype === 'movie' ? 'http://otis.ddns.net:5000/movierequest'
      : 'http://otis.ddns.net:5000/tvrequest';
  },

  getUrl = function() {
    return $scope.searchtype === 'movie' ? 'http://otis.ddns.net:5000/moviesearch'
      : 'http://otis.ddns.net:5000/tvsearch';
  },

  completeRequest = function(response) {
    $scope.searchresults = response.data.movies;
    if(!$scope.searchresults){
      $scope.searchresults = response.data.tv_shows;
    }
    $scope.loading = false;
  },

  cancelRequest = function() {
    if($scope.canceller) {
      $scope.canceller.resolve('user cancelled');
    }

    $scope.loading = false;
    $scope.canceller = $q.defer();
  };

}
