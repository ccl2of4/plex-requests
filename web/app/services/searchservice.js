plexRequests.factory('searchService', ['$http', 'envService',
    function SearchService($http, envService) {

  function movies(query, canceller, completion) {
    $http({
      url : getUrl('/moviesearch'),
      method : 'GET',
      params : {query : query},
      timeout : canceller.promise
    }).then(function(data) {
      completion(data.data.movies);
    });
  };

  function tvshows(query, canceller, completion) {
    $http({
      url : getUrl('/tvsearch'),
      method : 'GET',
      params : {query : query},
      timeout : canceller.promise
    }).then(function(data) {
      completion(data.data.tv_shows);
    });
  };

  function getUrl(endpoint) {
    return envService.read('apiBaseUrl') + endpoint;
  };

  return {
    movies : movies,
    tvshows : tvshows
  };

}]);
