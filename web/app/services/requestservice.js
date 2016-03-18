plexRequests.factory('requestService', ['$http',
    function RequestService($http) {

  function getAll(completion) {
    $http({
      url : '/requests',
      method : 'GET',
    }).then(function(data) {
      completion(data.data);
    });
  }

  function requestItem(item, completion) {
    $http({
      url : '/requests',
      method : 'POST',
      data : {item : item}
    }).then(function(response){
      completion();
    });
  };

  function deleteRequest(item, completion) {
    $http({
      url : '/requests/' + item['request_id'],
      method : 'DELETE',
      data : {item : item},
      headers: {'Content-Type': 'application/json' }
    }).then(function(response){
      completion();
    });
  };

  return {
    getAll : getAll,
    requestItem : requestItem,
    deleteRequest : deleteRequest
  };

}]);
