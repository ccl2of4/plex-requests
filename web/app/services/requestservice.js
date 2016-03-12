plexRequests.factory('requestService', ['$http', 'envService',
    function RequestService($http, envService) {

  function getAll(completion) {
    $http({
      url : getUrl('/requests'),
      method : 'GET',
    }).then(function(data) {
      completion(data.data);
    });
  }

  function requestItem(item, completion) {
    $http({
      url : getUrl('/requests'),
      method : 'POST',
      data : {item : item}
    }).then(function(response){
      completion();
    });
  };

  function deleteRequest(item, completion) {
    $http({
      url : getUrl('/requests/' + item['request_id']),
      method : 'DELETE',
      data : {item : item},
      headers: {'Content-Type': 'application/json' }
    }).then(function(response){
      completion();
    });
  };

  function getUrl(endpoint) {
    return envService.read('apiBaseUrl') + endpoint;
  };

  return {
    getAll : getAll,
    requestItem : requestItem,
    deleteRequest : deleteRequest
  };

}]);
