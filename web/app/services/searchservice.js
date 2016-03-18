plexRequests.factory('searchService', ['$http', '$q',
    function SearchService($http, $q) {

  function movies(query, completion) {
    canceler = $q.defer();
    $http({
      url : '/moviesearch',
      method : 'GET',
      params : {query : query},
      timeout : canceler.promise
    }).then(function(data) {
      completion(data.data['movies']);
    });
    return canceler;
  };

  function tvshows(query, completion) {
    canceler = $q.defer();
    $http({
      url : '/tvsearch',
      method : 'GET',
      params : {query : query},
      timeout : canceler.promise
    }).then(function(data) {
      completion(data.data['tv_shows']);
    });
    return canceler;
  };

  function cancel(canceler) {
    canceler.resolve();
  }

  return {
    movies : movies,
    tvshows : tvshows,
    cancel : cancel
  };

}]);
