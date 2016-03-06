plexRequests.controller('RequestController', ['$rootScope', '$scope', '$q', 'searchService', 'requestService',
    function RequestController($rootScope, $scope, $q, searchService, requestService) {

  $scope.searchtype = 'movie';

  $scope.$watch('query', function(query) {
    refresh(query);
  });

  $scope.$watch('searchtype', function(searchType) {
    refresh($scope.query);
  });

  $rootScope.$on('show_item', function(event, request) {
    console.log(request.type);
    $scope.searchtype = request.type;
    $scope.query = request.name;
  });

  $scope.setSearchType = function(type) {
    $scope.searchtype = type;
  }

  $scope.add = function(searchresult) {
    $scope.loading = true;
    requestService.request_item(searchresult, function() {
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
    if ($scope.searchtype === 'movie') {
      searchMovies(query);
    } else {
      searchTV(query);
    }
  },

  searchTV = function(query) {
    searchService.tvshows(query, $scope.canceller,
      completeRequest);
  },

  searchMovies = function(query) {
    searchService.movies(query, $scope.canceller,
      completeRequest);
  }

  postParams = function(searchresult) {
    return $scope.searchtype == 'movie' ?
      { movie : searchresult } :
      { tv_show : searchresult };
  },

  completeRequest = function(searchresults) {
    $scope.loading = false;
    $scope.searchresults = searchresults;
  },

  cancelRequest = function() {
    if($scope.canceller) {
      $scope.canceller.resolve('user cancelled');
    }

    $scope.loading = false;
    $scope.canceller = $q.defer();
  };
}]);
