plexRequests.factory('apiService', [
  function apiService() {

  return {
    buildUrl : buildUrl,
  };

  function buildUrl() {
    var res = '/api';
    for (var i = 0; i < arguments.length; ++i) {
      res += arguments[i];
    }
    return res;
  };

}]);
