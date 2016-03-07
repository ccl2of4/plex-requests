plexRequests.factory('requestService', ['$http', 'envService',
    function RequestService($http, envService) {

  function get_all(completion) {
    $http({
      url : baseUrl()  + '/requests',
      method : 'GET',
    }).then(function(data) {
      completion(data.data);
    });
  }

  function request_item(item, completion) {
    $http({
      url : baseUrl() + '/requests',
      method : 'POST',
      data : {item : item}
    }).then(function(response){
      completion();
    });
  };

  function delete_request(item, completion) {
    $http({
      url : baseUrl() + '/requests',
      method : 'DELETE',
      data : {item : item},
      headers: {'Content-Type': 'application/json' }
    }).then(function(response){
      completion();
    });
  }

  function baseUrl() {
    return envService.read('apiBaseUrl');
  }

  return {
    get_all : get_all,
    request_item : request_item,
    delete_request : delete_request
  };

}]);
