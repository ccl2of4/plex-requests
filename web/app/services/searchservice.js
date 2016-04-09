plexRequests.factory('searchService', ['$http', '$q', 'apiService', 'apiService',
    function SearchService($http, $q, api) {

  return {
    movies : movies,
    tvshows : tvshows,
    cancel : cancel
  };

  function movies(query, completion) {
    canceler = $q.defer();
    $http({
      url : api.buildUrl('/movies'),
      method : 'GET',
      params : {query : query},
      timeout : canceler.promise
    }).then(function(data) {
      completion(data.data);
    });
    return canceler;
  };

  function tvshows(query, completion) {
    canceler = $q.defer();
    $http({
      url : api.buildUrl('/tvshows'),
      method : 'GET',
      params : {query : query},
      timeout : canceler.promise
    }).then(function(data) {
      completion(data.data);
    });
    return canceler;
  };

  function cancel(canceler) {
    canceler.resolve();
  };

}]);
