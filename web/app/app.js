var plexRequests = angular.module('plexRequests', ['ngRoute']);

plexRequests.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/', {
        templateUrl: 'app/views/main.html',
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);
