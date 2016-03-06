plexRequests.factory('requestService', ['$http', 'urlResolver',
    function RequestService($http, urlResolver) {

  function get_all(completion) {
    $http({
      url : urlResolver.base_url + '/requests',
      method : 'GET',
    }).then(function(data) {
      completion(data.data);
    });
  }

  function request_item(item, completion) {
    $http({
      url : urlResolver.base_url + '/requests',
      method : 'POST',
      data : {item : item}
    }).then(function(response){
      completion();
    });
  };

  function delete_request(item, completion) {
    $http({
      url : urlResolver.base_url + '/requests',
      method : 'DELETE',
      data : {item : item},
      headers: {'Content-Type': 'application/json' }
    }).then(function(response){
      completion();
    });
  }

  return {
    get_all : get_all,
    request_item : request_item,
    delete_request : delete_request
  };

}]);
