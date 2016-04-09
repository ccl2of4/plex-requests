plexRequests.factory('requestService', ['$http', 'apiService',
    function RequestService($http, api) {

  return {
    getAll : getAll,
    requestItem : requestItem,
    deleteRequest : deleteRequest
  };

  function getAll(completion) {
    $http({
      url : api.buildUrl('/requests'),
      method : 'GET',
    }).then(function(data) {
      completion(data.data);
    });
  };

  function requestItem(item, completion) {
    $http({
      url : api.buildUrl('/requests'),
      method : 'POST',
      data : item
    }).then(function(response){
      completion();
    });
  };

  function deleteRequest(item, completion) {
    $http({
      url : api.buildUrl('/requests/', item['request_id']),
      method : 'DELETE',
      data : item,
      headers: {'Content-Type': 'application/json' }
    }).then(function(response){
      completion();
    });
  };

}]);
