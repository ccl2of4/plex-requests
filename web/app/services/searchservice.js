plexRequests.factory('searchService', ['$http', 'envService',
    function SearchService($http, envService) {

  function movies(query, canceller, completion) {
    $http({
      url : baseUrl() + '/moviesearch',
      method : 'GET',
      params : {query : query},
      timeout : canceller.promise
    }).then(function(data) {
      completion(data.data.movies);
    });
  };

  function tvshows(query, canceller, completion) {
    $http({
      url : baseUrl() + '/tvsearch',
      method : 'GET',
      params : {query : query},
      timeout : canceller.promise
    }).then(function(data) {
      completion(data.data.tv_shows);
    });
  };


  function baseUrl() {
    return envService.read('apiBaseUrl');
  }

  return {
    movies : movies,
    tvshows : tvshows
  };

}]);
