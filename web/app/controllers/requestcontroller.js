plexRequests.controller('RequestController', ['$rootScope', '$scope', 'searchService', 'requestService',
    function RequestController($rootScope, $scope, searchService, requestService) {

  (function init() {
    $scope.searchType = 'movie';

    $scope.$watch('query', function(query) {
      updateSearchResults(query);
    });

    $scope.$watch('searchType', function(searchType) {
      updateSearchResults($scope.query);
    });

    $rootScope.$on('showItem', function(event, request) {
      $scope.searchType = request.type;
      $scope.query = request.name;
    });
  })();

  function setSearchType(type) {
    $scope.searchType = type;
  };

  function requestItem(searchResult) {
    $scope.loading = true;
    requestService.requestItem(searchResult, function() {
      $scope.loading = false;
      $rootScope.$emit('refreshNeeded');
    });
  };

  function updateSearchResults(query) {
    cancelPreviousRequest();
    if (query) {
      $scope.canceler = search(query);
    } else {
      $scope.searchResults = [];
    }
  };

  function search(query) {
    $scope.loading = true;

    if (isSearchType('movie')) {
      return searchMovies(query);
    } else {
      return  searchTV(query);
    }
  };

  function searchTV(query) {
    return searchService.tvshows(query, completeRequest);
  };

  function searchMovies(query) {
    return searchService.movies(query, completeRequest);
  };

  function completeRequest(searchResults) {
    $scope.loading = false;

    $scope.searchResults = searchResults;
  };

  function cancelPreviousRequest() {
    $scope.loading = false;

    if ($scope.canceler) {
      searchService.cancel($scope.canceler);
      delete $scope.canceler;
    }
  };

  function isSearchType(type) {
    return $scope.searchType === type;
  }

  $scope.setSearchType = setSearchType;
  $scope.isSearchType = isSearchType;
  $scope.requestItem = requestItem;

}]);
