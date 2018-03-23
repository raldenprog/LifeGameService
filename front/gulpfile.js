// Include gulp
var gulp = require('gulp'),
    // Include Our Plugins
    less = require('gulp-less'),
    postcss = require('gulp-postcss'),
    autoprefixer = require('autoprefixer');

gulp.task('css', function () {
    gulp
        .src('./app/less/main.less')
        .pipe(less({ strictMath: true }))
        .pipe(postcss([
            autoprefixer({ browsers: ['> 1%', 'IE 9', 'IE 10']})
        ]))
        .pipe(gulp.dest('./app/css'));
});

gulp.task('watch', function () {
    gulp.watch('./app/less/**/*.less', ['css']);
});

gulp.task('default', ['css', 'watch']);
