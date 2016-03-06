plexRequests.factory('searchService', ['$http', 'urlResolver',
    function SearchService($http, urlResolver) {

  function movies(query, canceller, completion) {
    $http({
      url : urlResolver.base_url + '/moviesearch',
      method : 'GET',
      params : {query : query},
      timeout : canceller.promise
    }).then(function(data) {
      completion(data.data.movies);
    });
  };

  function tvshows(query, canceller, completion) {
    $http({
      url : urlResolver.base_url + '/tvsearch',
      method : 'GET',
      params : {query : query},
      timeout : canceller.promise
    }).then(function(data) {
      completion(data.data.tv_shows);
    });
  };

  return {
    movies : movies,
    tvshows : tvshows
  };

}]);
