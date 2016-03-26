module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    ngtemplates: {
      app: {
        src: 'app/*/**.html',
        dest: 'templates.js'
      },
      options: {
        module: 'plexRequests'
      }
    }
  });

  grunt.loadNpmTasks('grunt-angular-templates');

  grunt.registerTask('default', ['ngtemplates']);

};
