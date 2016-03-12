plexRequests.factory('searchService', ['$http', '$q', 'envService',
    function SearchService($http, $q, envService) {

  function movies(query, completion) {
    canceler = $q.defer();
    $http({
      url : getUrl('/moviesearch'),
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
      url : getUrl('/tvsearch'),
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

  function getUrl(endpoint) {
    return envService.read('apiBaseUrl') + endpoint;
  };

  return {
    movies : movies,
    tvshows : tvshows,
    cancel : cancel
  };

}]);
