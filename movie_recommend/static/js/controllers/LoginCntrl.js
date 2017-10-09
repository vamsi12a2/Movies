angular.module("movies").
controller('LoginCntrl',['$scope','Auth','$location',function($scope,Auth,$location){

    $scope.login =  function(username,password)
    {
        console.log('login method')
        Auth.login(username,password).then(
            function(res)
            {
                
                $location.path("/user")
            }
        )
    }
}])