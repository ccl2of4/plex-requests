var plexRequests = angular.module('plexRequests', ['environment']).
  config(function(envServiceProvider) {
  // set the domains and variables for each environment
    envServiceProvider.config({
      domains: {
        development: ['localhost'],
        production: ['otis.ddns.net']
      },
      vars: {
        development: {
          apiBaseUrl: 'http://otis.ddns.net',
        },
        production: {
          apiBaseUrl: 'http://localhost',
        }
      }
    });

  // run the environment check, so the comprobation is made
  // before controllers and services are built
  envServiceProvider.check();
  });
