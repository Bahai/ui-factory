// be in the factory directory and run 'foundation watch'

var gulp = require('gulp');
var sass = require('gulp-sass');
var $ = require('gulp-load-plugins')();

var sassPaths = [
    'bower_components/normalize.scss/sass',
    'bower_components/foundation-sites/scss',
    'bower_components/motion-ui/src'
];

gulp.task('sass', function() {
    return gulp.src('static/stylesheets/sass/main.sass')
        .pipe($.sass({
                includePaths: sassPaths,
                outputStyle: 'compressed'
            })
            .on('error', $.sass.logError))
        .pipe($.autoprefixer({
            browsers: ['last 2 versions', 'ie >= 9']
        }))
        .pipe(gulp.dest('static/stylesheets/css'));
});

gulp.task('foundation', function() {
    return gulp.src('static/stylesheets/sass/foundation.scss')
        .pipe($.sass({
                includePaths: sassPaths,
                outputStyle: 'extended'
            })
            .on('error', $.sass.logError))
        .pipe(gulp.dest('static/stylesheets/css'));
});

gulp.task('default', ['sass'], function() {
    gulp.watch(['static/stylesheets/sass'], ['sass']);
});