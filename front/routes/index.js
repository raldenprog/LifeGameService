var express = require('express');
var router = express.Router();
var cookieParser = require('cookie-parser');


/* GET home page. */
router.get('/', function(req, res, next) {


    if (typeof req.cookies.UUID != 'string') {
        res.redirect('/login/');
    } else {
        res.redirect('/competitions-list/');
        //res.render('index', { UUIDset: true, title: 'Express', condition: true });
    }
});

router.get('/newtask', function(req, res, next) {
    res.render('create-task', { UUIDset: true, title: 'Express', condition: true });
});


router.get('/competition/:id/:competitionSection', function(req, res, next) {
    var competitionSection = req.params.competitionSection;
    if (typeof req.cookies.UUID != 'string') {
        res.redirect('/login/');
    } else {
        switch (competitionSection) {
            case 'info':
                res.render('competition-info', { UUIDset: true, competitionId: req.params.id });
                break;
            case 'tasks':
                res.render('competition-tasks', { UUIDset: true, competitionId: req.params.id });
                break;
            case 'rating':
                res.render('competition-rating', { UUIDset: true, competitionId: req.params.id });
                break;
            default:
                res.redirect('/competition/:id/info');
                break;
        }
    }
});

router.get('/competition/:id/', function(req, res, next) {
        res.redirect('/competition/' + req.params.id + '/info');
});

router.get('/competition/', function(req, res, next) {
    res.redirect('/competitions-list/');
});

router.get('/competitions-list/', function(req, res, next) {
    var UUIDset = true;
    if (typeof req.cookies.UUID != 'string') {
        UUIDset = false;
    }

    if (typeof req.cookies.UUID != 'string') {
        res.redirect('/login/');
    } else {
        res.render('competitions-list', { UUIDset: UUIDset, output: req.params.id });
    }


});

router.get('/reg/', function(req, res, next) {
    //res.cookie('UUID', 1);
    //res.clearCookie('name');
    console.log(req.cookies.name);

    if (typeof req.cookies.UUID != 'string') {
        res.render('reg', { cookiesUUID: req.cookies.UUID });
    } else {
        res.redirect('/competitions-list/');
    }
});

router.get('/login/', function(req, res, next) {
    //res.cookie('UUID', 1);
    //res.clearCookie('name');
    //console.log(req.cookies.name);
    console.log(typeof req.cookies.UUID);
    if (typeof req.cookies.UUID != 'string') {
        res.render('login', { title: 'Авторизация' });
    } else {
        console.log("redirect");
        res.redirect('/competitions-list/');
    }
});

router.get('/account/', function(req, res, next) {
    console.log("cookie");
    console.log(req.cookies.UUID); // выводит значение
    console.log(typeof req.cookies.UUID); // выводит тип кукисов
    console.log("cookie");

    if (typeof req.cookies.UUID != 'string') {
        res.redirect('/login/');
    } else {
        res.render('account', { UUIDset: true, title: 'Персональная страница' });
    }
});


router.use('/css', express.static('app/css'));
router.use('/img', express.static('app/img'));
router.use('/js', express.static('app/js'));

module.exports = router;
