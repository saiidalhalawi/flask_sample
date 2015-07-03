module.exports = function(grunt) {
  //グラントタスクの設定
  grunt.initConfig({

    pkg: grunt.file.readJSON('package.json'),
    /**
     * Set project object
     */
    project: {
      app: 'atnd',
      assets: '<%= project.atnd %>/assets',
      src: '<%= project.assets %>/src',
      css: [
        '<%= project.src %>/scss/style.scss'
      ],
      js: [
        '<%= project.src %>/js/*.js'
      ]
    },
    //watchの設定
    watch: {
      dev: {
        files: []
      }
    }
  });
  //プラグインの読み込み
  //grunt.loadNpmTasks('grunt-contrib-watch');
};