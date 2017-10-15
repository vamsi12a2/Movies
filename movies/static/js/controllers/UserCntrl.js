angular.module("movies").
controller('UserCntrl',['$scope','Auth','$location','$http','User',function($scope,Auth,$location,$http,User){
 
    User.get_page().then(function(res){
       $scope.data = res.data
   })     
    $scope.goto = function(path){
        $location.path(path)
    }   
    $scope.logout = function(){
        Auth.logout().then(function(res){
            $location.path("/")
        })
    }
    $scope.reload = function(){

        User.get_page().then(function(res){
            $scope.data = res.data
        })     
    }

}])