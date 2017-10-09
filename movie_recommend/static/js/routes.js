angular.module("movies").config(
    ['$routeProvider',function($routeProvider){
    
        $routeProvider
        .when('/',{controller:'LoginCntrl',templateUrl:'/static/templates/login.html'})
        .when('/register',{controller:'RegisterCntrl', templateUrl:'/static/templates/register.html'})
        .when('/user',{controller:'UserCntrl',templateUrl:'/static/templates/user.html'})
    }
    ])
    