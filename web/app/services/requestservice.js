plexRequests.factory('requestService', ['$http', 'envService',
    function RequestService($http, envService) {

  function get_all(completion) {
    $http({
      url : getUrl('/requests'),
      method : 'GET',
    }).then(function(data) {
      completion(data.data);
    });
  }

  function request_item(item, completion) {
    $http({
      url : getUrl('/requests'),
      method : 'POST',
      data : {item : item}
    }).then(function(response){
      completion();
    });
  };

  function delete_request(item, completion) {
    $http({
      url : getUrl('/requests'),
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
    get_all : get_all,
    request_item : request_item,
    delete_request : delete_request
  };

}]);
